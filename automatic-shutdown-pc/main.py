#!/usr/bin/env python

import logging
from view.gui import Gui
from model.task_model import TaskModel
from model.state_model import StateModel

# NUITKA
# doesnt work with tkinter - PySimpleGui library

# PYINSTALLER
# COULD USE pip install auto-py-to-exe GUI interface to the pyinstaller
# SLOW START                pyinstaller --onefile --noconsole --icon="resources\shutdown_icon.ico" main.py
# MUCH FASTER START, BUT FOLDER: pyinstaller --onedir --noconsole --icon="resources\shutdown_icon.ico" main.py
# pyinstaller.exe --noconfirm --onedir --windowed --name "Vypnout PC" --icon "resources/shutdown_icon.ico"
#     --add-data "resources;resources" main.py

# following explicit imports are neccessary because of pyinstaller's error
# ModuleNotFoundError: No module named 'tasks.restart_task' etc.
import tasks.shutdown_task
import tasks.restart_task
import tasks.remainder_task


TASKS_ACTIVE = ["tasks.shutdown_task.ShutdownTask", "tasks.restart_task.RestartTask", "tasks.remainder_task.RemainderTask"]
DEFAULT_TASK = "Shutdown"
DEFAULT_STR_AFTERDELTA = "00:30"
LOG_FILENAME = "shutdown.log"


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(filename=LOG_FILENAME, mode="a", encoding="utf-8")
        ],
    )

    logging.info("STARTING")

    task_model = TaskModel(TASKS_ACTIVE)
    state_model = StateModel(DEFAULT_STR_AFTERDELTA, DEFAULT_TASK)
    gui = Gui(task_model, state_model)
    gui.run()

    logging.info("FINISHED\n\n")
