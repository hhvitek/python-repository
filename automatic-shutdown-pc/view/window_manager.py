#!/usr/bin/env python

import logging
from .window_creator import WindowCreator
from model.timedelta_manager import TimedeltaManager


class WindowManager:
    """
    A class to manipulate existing window object, based on (depends)
    objects unique keys/identificators created by WindowCreator object
    """

    def __init__(self, task_model, state_model):
        self.task_model = task_model
        self.state_model = state_model

        self.window_creator = None
        self.window = self._create_window()

        self.timedelta_manager = TimedeltaManager()

        self.is_configuring_state = None
        self.restore_window_state_from_model()

    def _create_window(self):
        tasks = self.task_model.get_tasks()
        self.window_creator = WindowCreator(tasks)
        return self.window_creator.create()

    def get_window(self):
        return self.window

    def echo_info_to_user(self, info_message):
        status_bar = self.window["status_bar"]
        status_bar.update(value=info_message)
        status_bar.expand(expand_x=True, expand_row=True)

    def echo_error_to_user(self, error_message):
        self.echo_info_to_user(error_message)
        error_popup = self.window_creator.create_error_popup(error_message)

    def restore_window_state_from_model(self):
        selected_task_name = self.state_model.get_selected_task_name()
        timedelta_manager = self.state_model.get_timedelta_delay()
        scheduled_task_name = self.state_model.get_scheduled_task_name()

        if selected_task_name is not None:
            self.window["combo_tasks"].update(value=selected_task_name)

        if scheduled_task_name is not None:
            self.update_countdown_using_timedelta_delay(timedelta_manager)
            self.set_countdown_state()
        else:
            self.spin_timing_changed()
            self.set_configuring_state()

    def set_configuring_state(self):
        """
            * Cannot choose another task
            * Cannot change timing
            * Cannot schedule another task
            * Can cancel scheduled task / stop countdown / reset window
        """
        if not self._is_in_configuring_state():
            logging.debug("Setting configuring state.")
            self._set_window_state(True)

    def _set_window_state(self, configuring=True):
        self._can_choose_another_task(configuring)
        self._can_change_timing(configuring)
        self._can_schedule_another_task(configuring)
        self._can_change_parameter(configuring)
        self.is_configuring_state = configuring

    def _can_choose_another_task(self, can=True):
        combo = self.window["combo_tasks"]
        combo.update(disabled=not can, readonly=not can)

    def _can_change_timing(self, can=True):
        spin_timing = self.window["spin_timing"]
        # BUG??? spin_timing.update(disabled=not can)

    def _can_schedule_another_task(self, can=True):
        button_submit = self.window["button_submit"]
        button_submit.update(disabled=not can)

        button_cancel = self.window["button_cancel"]
        button_cancel.update(disabled=can)

    def _can_change_parameter(self, can=True):
        input_parameter = self.window["input_parameter"]
        input_parameter.update(disabled=not can)

    def _is_in_configuring_state(self):
        return self.is_configuring_state

    def set_countdown_state(self):
        """
            * Can choose another task
            * Can change timing
            * Can schedule another task
            * Cannot cancel scheduled task / stop countdown / reset window
        """
        if self._is_in_configuring_state():
            logging.debug("Setting countdown state.")
            self._set_window_state(False)

    def spin_timing_changed(self):
        # 00:00
        timing = self.window.Element("spin_timing").Get()
        self.timedelta_manager.set_when_elapsed_using_afterdelta(timing)
        self.update_countdown_using_timedelta_delay(self.timedelta_manager)

    def update_countdown_using_timedelta_delay(self, timedelta_delay=None):

        self._update_countdown_when_elapsed(timedelta_delay)
        self._update_countdown_remaining(timedelta_delay)

    def _update_countdown_when_elapsed(self, timedelta_delay=None):

        if timedelta_delay is None:
            timedelta_delay = self.timedelta_manager

        text_when_elapsed = self.window.Element("text_countdown_when_elapsed")

        when_elapsed = timedelta_delay.get_when_elapsed()

        text_when_elapsed.Update(value=when_elapsed)

    def _update_countdown_remaining(self, timedelta_delay=None):

        if timedelta_delay is None:
            timedelta_delay = self.timedelta_manager

        text_remaininig = self.window.Element("text_countdown_remaining")
        remaining = timedelta_delay.get_remaining()

        text_remaininig.Update(value=remaining)