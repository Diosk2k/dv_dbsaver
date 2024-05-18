@echo off
REM Install required Python modules for the script

REM Install mysql-connector-python
pip install mysql-connector-python

REM Install configparser
pip install configparser

REM Install requests
pip install requests

REM Print a message when installation is completed
echo Required Python modules have been installed.

REM Check if the "backups" folder exists. If not, create the folder.
if not exist "%~dp0backups" (
    mkdir "%~dp0backups"
    echo Folder "backups" has been created.
) else (
    echo Folder "backups" already exists.
)

REM Start the Python script
cd /d "%~dp0"
python backup_script.py

REM Wait for user interaction before closing the window
pause

REM Wait for 5 seconds to allow the user to see the message before closing the window
timeout /t 5 >nul
