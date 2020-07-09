#!/usr/bin/env python

import logging
from view.gui3 import Gui
from model.model import Model
from model.class_loader import ClassLoader


TASKS_ACTIVE = ["tasks.shutdown_task.ShutdownTask", "tasks.restart_task.RestartTask"]


def get_tasks_from_tasks_modules(tasks_modules):

    loader = ClassLoader()
    tasks = []
    for task_module in tasks_modules:
        task = loader.from_string(task_module)
        tasks.append(task)

    return tasks


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    tasks = get_tasks_from_tasks_modules(TASKS_ACTIVE)
    model = Model(tasks)

    gui = Gui()
    gui.run()

