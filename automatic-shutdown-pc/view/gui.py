#!/usr/bin/env python

import logging

from .window_manager import WindowManager
from tasks.task_exception import TaskError


class Gui:
    """A UI defined using PySimpleGUI library"""

    def __init__(self, task_model, state_model):
        self.task_model = task_model
        self.state_model = state_model

        self.window_manager = WindowManager(task_model, state_model)
        self.window = self.window_manager.get_window()

        self.window_manager.restore_window_state_from_model()

    def _new_task_chosen_by_user(self, task_name):
        logging.info(f"The new task chosen: <{task_name}>")
        self.state_model.set_selected_task_name(task_name)
        self.window_manager.echo_info_to_user(f"Vybrána nová akce: <{task_name}>")

    # 00:00
    def _new_task_scheduled_by_user(self, task_name, str_afterdelta):
        logging.info(f"The new task scheduled: <{task_name}>:<{str_afterdelta}>")

        self.state_model.set_selected_task_name(task_name)
        self.state_model.set_scheduled_task(task_name, str_afterdelta)

        self.window_manager.echo_info_to_user(
            f"Načasována akce: <{task_name}>:<{str_afterdelta}>"
        )

    def _tick_timeout_event(self):
        if self.state_model.is_scheduled():
            timedelta_delay = self.state_model.get_timedelta_delay()
            self.window_manager.update_countdown_using_timedelta_delay(timedelta_delay)

            if self.state_model.has_elapsed():
                self._execute_scheduled_task()
                self.state_model.restore_initial_state()
                self.window_manager.restore_window_state_from_model()

    def _execute_scheduled_task(self):
        scheduled_task_name = self.state_model.get_scheduled_task_name()
        try:
            result_message = self.task_model.execute_task(scheduled_task_name)
            self.window_manager.echo_info_to_user(
                f"{scheduled_task_name} executed succesfully. {result_message}"
            )
        except ValueError as e:
            logging.error(f"VALUE_ERROR {e}")
            self.window_manager.echo_error_to_user()(
                f"{scheduled_task_name} execution failure. Unknown task."
            )
        except TaskError as e:
            self.window_manager.echo_error_to_user()(
                f"{scheduled_task_name} execution failure. {e}"
            )

    def _cancel_task(self):
        if self.state_model.is_scheduled():
            self.state_model.cancel_scheduled_task()
            self.window_manager.restore_window_state_from_model()
            logging.info(f"The scheduled task cancelled.")
            self.window_manager.echo_info_to_user(f"Načasovaná akce zrušena.")

    def run(self):
        while True:
            event, values = self.window.Read(timeout=1000, timeout_key="timeout")

            if event is None or event == "Exit" or event == "button_exit":
                break
            elif event == "combo_tasks":
                task_name = values["combo_tasks"]
                self._new_task_chosen_by_user(task_name)
            elif event == "spin_timing":
                self.window_manager.spin_timing_changed()
            elif event == "timeout":
                self._tick_timeout_event()
            elif event == "button_submit":
                task_name = values["combo_tasks"]
                str_afterdelta = values["spin_timing"]
                self._new_task_scheduled_by_user(task_name, str_afterdelta)
            elif event == "button_cancel":
                self._cancel_task()

            if event != "timeout":
                logging.info(event)

        self.window.Close()
