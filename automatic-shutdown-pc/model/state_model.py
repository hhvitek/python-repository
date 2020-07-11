#!/usr/bin/env python

import logging
from .timedelta_manager import TimedeltaManager

DEFAULT_STR_AFTERDELTA = "00:30"


class StateModel:
    """
    Represents the current state (status) of this application.
    This is dynamic state, possibly can be stored in database for persistence
    """

    def __init__(
        self,
        default_str_afterdelta=DEFAULT_STR_AFTERDELTA,
        default_selected_task_name=None,
    ):
        self.default_selected_task_name = default_selected_task_name
        self.default_str_afterdelta = default_str_afterdelta

        self.timedelta_delay = None
        self.scheduled_task_name = None
        self.selected_task_name = None

        self.restore_initial_state()

    def restore_initial_state(self):
        logging.debug("Restoring initial StateModel state.")
        self.set_scheduled_task(None)
        self.set_selected_task_name(self.default_selected_task_name)

    def set_selected_task_name(self, task_name):
        logging.debug(f"The new task selected: <{task_name}>.")
        self.selected_task_name = task_name

    def get_selected_task_name(self):
        return self.selected_task_name

    def set_scheduled_task(self, task_name, str_afterdelta=DEFAULT_STR_AFTERDELTA):
        logging.debug(f"The new task scheduled: <{task_name}>:<{str_afterdelta}>")
        self.scheduled_task_name = task_name
        self.timedelta_delay = TimedeltaManager(str_afterdelta)

    def get_scheduled_task_name(self):
        """
            Returns None if no task is scheduled
        """
        return self.scheduled_task_name

    def get_timedelta_delay(self):
        """
            Returns timedelta_manager if scheduled
                    None otherwise
        """
        return self.timedelta_delay

    def has_elapsed(self):
        return self.is_scheduled() and self.timedelta_delay.has_elapsed()

    def is_scheduled(self):
        return self.timedelta_delay is not None and self.scheduled_task_name is not None

    def cancel_scheduled_task(self):
        if self.is_scheduled():
            logging.info(
                f"Scheduled task cancelled: <{self.get_scheduled_task_name()}>"
            )
            self.restore_initial_state()
