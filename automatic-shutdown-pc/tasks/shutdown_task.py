#!/usr/bin/env python

from .task import Task
import logging


class ShutdownTask(Task):
    """this task will shutdown the computer"""

    def __init__(self):
        name = "Shutdown"
        description = "This will shutdown the computer."

        Task.__init__(self, name, description)

    def execute(self):
        logging.info("Execution ShutDown...")
        return "OK"
