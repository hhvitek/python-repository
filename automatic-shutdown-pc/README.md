# Required libraries
pysimplegui, pyinstaller

# NUITKA
doesn't work with tkinter - PySimpleGui GUI library

# PYINSTALLER
COULD USE pip install auto-py-to-exe GUI interface to the pyinstaller
SLOW START  
```shell
pyinstaller --onefile --noconsole --icon="resources\shutdown_icon.ico" main.py
```

MUCH FASTER START, BUT FOLDER: 
```shell
python -m PyInstaller ^
    --noconfirm ^
    --onedir ^
    --windowed ^
    --name "%python_script_name%" ^
    --icon "resources\shutdown_icon.ico" ^
    --add-data "resources;resources" ^
    main.py
```

# !!!!!!!!the following explicit imports are required 
to be in main.py file for pyinstaller to work, 
OR pyinstaller can be used with multiple --hidden-import flags instead
```python
import tasks.shutdown_task
import tasks.restart_task
import tasks.remainder_task
```
ModuleNotFoundError: No module named 'tasks.restart_task' etc.
