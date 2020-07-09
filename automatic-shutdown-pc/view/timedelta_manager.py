#!/usr/bin/env python

from datetime import timedelta, datetime


class TimedeltaManager:

    # 00:00
    def __init__(self):
        self.when_elapsed = datetime.now()

    # 00:00
    def set_when_elapsed_using_afterdelta(self, str_afterdelta):
        hours, minutes = str_afterdelta.split(":", 1)

        after_delta = timedelta(hours=float(hours), minutes=float(minutes) + 1.0)

        self.when_elapsed = datetime.now() + after_delta

    def get_when_elapsed(self, format_str="%H:%M"):
        return self.when_elapsed.strftime(format_str)

    def get_remaining(self, format_str="%H:%M"):
        after_delta = self.when_elapsed - datetime.now()
        return self._timedelta_to_string(after_delta)

    def _timedelta_to_string(self, time_delta):
        seconds = time_delta.total_seconds()
        return self._get_hours_minutes(seconds)

    def _get_hours_minutes(self, seconds):
        onehour_in_minutes = 60
        minutes = int(seconds // 60)

        hour, minutes = divmod(minutes, onehour_in_minutes)

        return f"{hour:02}:{minutes:02}"
