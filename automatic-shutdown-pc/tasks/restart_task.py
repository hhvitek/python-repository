#!/usr/bin/env python

import logging

from .task import Task
from .task_exception import TaskError


class RestartTask(Task):
    """this task will restart the computer"""

    def __init__(self):
        name = "Restart"
        description = "This will restart the computer."

        Task.__init__(self, name, description)

    def execute(self):
        logging.info("Execution Restart...")
        raise TaskError("Not Implemented!")
