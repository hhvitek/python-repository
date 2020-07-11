:: This little script uses PyInstaller to create executable file from main.py application entry point.
:: The result is stored into dist/ folder
:: Automatically creates shortcut

@ECHO OFF
TITLE "Creates scripts .exe file"
ECHO Starting building...
ECHO.

SET "python_script_name=Vypnout PC"

python -m PyInstaller --noconfirm --onedir --windowed --name "%python_script_name%" --icon "resources\shutdown_icon.ico" --add-data "resources;resources" main.py

ECHO.
ECHO Cleaning temporary files...
RMDIR /S /Q "build\"
DEL /Q "%python_script_name%.spec"

ECHO.
ECHO Creating shortcut...
Echo.

SET script="$shortcut=(New-Object -COM WScript.Shell).CreateShortcut('%python_script_name%.lnk'); "^
            "$shortcut.TargetPath='%~dp0\dist\%python_script_name%\%python_script_name%.exe'; "^
            "$shortcut.WorkingDirectory='%~dp0\dist\%python_script_name%\'; "^
            "$shortcut.Save()

POWERSHELL -Command %script%
Echo Finished
Echo.

PAUSE