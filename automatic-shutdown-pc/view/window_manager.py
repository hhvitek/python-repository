#!/usr/bin/env python

from .timedelta_manager import TimedeltaManager


class WindowManager:
    def __init__(self, window):
        self.window = window
        self.timedelta_manager = TimedeltaManager()

    def get_selected_item(self):
        pass

    def spin_timing_changed(self):
        # 00:00
        timing = self.window.Element("spin_timing").Get()
        self.timedelta_manager.set_when_elapsed_using_afterdelta(timing)
        self._update_countdown_when_elapsed()
        self._update_countdown_remaining()

    def _update_countdown_when_elapsed(self):
        text_when_elapsed = self.window.Element("text_countdown_when_elapsed")
        when_elapsed = self.timedelta_manager.get_when_elapsed()

        text_when_elapsed.Update(value=when_elapsed)

    def _update_countdown_remaining(self):
        text_remaininig = self.window.Element("text_countdown_remaining")
        remaining = self.timedelta_manager.get_remaining()

        text_remaininig.Update(value=remaining)
