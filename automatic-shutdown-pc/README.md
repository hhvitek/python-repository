# python-repository

requires pysimplegui, pyinstaller

# NUITKA
# doesnt work with tkinter - PySimpleGui library

# PYINSTALLER
# COULD USE pip install auto-py-to-exe GUI interface to the pyinstaller
# SLOW START                pyinstaller --onefile --noconsole --icon="resources\shutdown_icon.ico" main.py
# MUCH FASTER START, BUT FOLDER: pyinstaller --onedir --noconsole --icon="resources\shutdown_icon.ico" main.py
# pyinstaller.exe --noconfirm --onedir --windowed --name "Vypnout PC" --icon "resources/shutdown_icon.ico"
#     --add-data "resources;resources" main.py

# !!!!!!!!the following explicit imports are required to be here for pyinstaller, otherwise pyinstaller can be
# used with multiple --hidden-import flags instead
# import tasks.shutdown_task
# import tasks.restart_task
# import tasks.remainder_task
# ModuleNotFoundError: No module named 'tasks.restart_task' etc.

import tasks.shutdown_task
import tasks.restart_task
import tasks.remainder_task