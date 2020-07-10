#!/usr/bin/env python


class TaskError(Exception):
    def __init__(self, message):
        self.message = message
