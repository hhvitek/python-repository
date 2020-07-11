#!/usr/bin/env python

import logging
from view.gui import Gui
from model.task_model import TaskModel
from model.state_model import StateModel

# NUITKA
# doesnt work with tkinter - PySimpleGui library

# PYINSTALLER
# COULD USE pip install auto-py-to-exe
# SLOW START                pyinstaller --onefile --noconsole --icon="resources\shutdown_icon.ico" main.py
# FASTER START, BUT FOLDER: pyinstaller --onedir --noconsole --icon="resources\shutdown_icon.ico" main.py
# pyinstaller.exe --noconfirm --onedir --windowed --name "Vypnout PC"
# --icon "resources/shutdown_icon.ico" --add-data "resources;resources"
# main.py

# explicit imports needed because pyinstaller's error
# ModuleNotFoundError: No module named 'tasks.restart_task'
import tasks.shutdown_task
import tasks.restart_task


TASKS_ACTIVE = ["tasks.shutdown_task.ShutdownTask", "tasks.restart_task.RestartTask"]
DEFAULT_STR_AFTERDELTA = "00:30"
LOG_FILENAME = "shutdown.log"


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(filename=LOG_FILENAME, mode="a", encoding="utf-8")
        ],
    )

    logging.info("STARTING")

    task_model = TaskModel(TASKS_ACTIVE)
    state_model = StateModel(DEFAULT_STR_AFTERDELTA)
    gui = Gui(task_model, state_model)
    gui.run()
