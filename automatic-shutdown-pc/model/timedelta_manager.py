#!/usr/bin/env python

from datetime import timedelta, datetime


class TimedeltaManager:

    # 00:00
    def __init__(self, str_afterdelta="00:00"):
        self.set_when_elapsed_using_afterdelta(str_afterdelta)

    def set_to_now(self):
        self.when_elapsed = datetime.now()

    # 00:00
    def set_when_elapsed_using_afterdelta(self, str_afterdelta):
        hours, minutes = str_afterdelta.split(":", 1)

        after_delta = timedelta(hours=float(hours), minutes=float(minutes))

        self.when_elapsed = datetime.now() + after_delta

    def get_when_elapsed(self, format_str="%H:%M"):
        return self.when_elapsed.strftime(format_str)

    def get_remaining(self):
        after_delta = self.when_elapsed - datetime.now()
        return self._timedelta_to_string(after_delta)

    def has_elapsed(self):
        return self.when_elapsed < datetime.now()

    def _timedelta_to_string(self, time_delta):
        seconds = time_delta.total_seconds()
        return self._get_hours_minutes_seconds(seconds)

    def _get_hours_minutes_seconds(self, seconds):
        if seconds > 0:
            onehour_in_minutes = 60
            minutes = int(seconds // 60)

            hour = int(minutes // onehour_in_minutes)
            minutes = int(minutes % onehour_in_minutes)
            seconds = int(seconds - (hour * 3600 + minutes * 60))

            return f"{hour:02}:{minutes:02}:{seconds:02}"
        else:
            return "00:00:00"
