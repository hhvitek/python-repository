#!/usr/bin/env python

from .task import Task
import logging


class RestartTasl(Task):
    """this task will restart the computer"""

    def __init__(self):
        name = "Restart"
        description = "This will restart the computer."

        Task.__init__(self, name, description)

    def execute(self):
        logging.info("Execution Restart...")
