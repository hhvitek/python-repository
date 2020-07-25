#!/usr/bin/env python

import logging
from .task import Task

import PySimpleGUI as sg


class RemainderTask(Task):
    """this task This will show any parameter in a popup window."""

    def __init__(self):
        name = "Remainder"
        description = "This will show any message in a popup window."

        Task.__init__(self, name, description, True)

    def execute(self, parameter):
        logging.debug("Execution Remainder...")

        sg.popup_ok(
            self.parameter,
            title="Information message",
            grab_anywhere=True,
            line_width=200,
        )
