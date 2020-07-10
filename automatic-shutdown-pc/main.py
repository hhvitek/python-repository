#!/usr/bin/env python

import logging
from view.gui import Gui
from model.task_model import TaskModel
from model.state_model import StateModel


TASKS_ACTIVE = ["tasks.shutdown_task.ShutdownTask", "tasks.restart_task.RestartTask"]
DEFAULT_STR_AFTERDELTA = "00:30"


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    task_model = TaskModel(TASKS_ACTIVE)
    state_model = StateModel(DEFAULT_STR_AFTERDELTA)
    gui = Gui(task_model, state_model)
    gui.run()
