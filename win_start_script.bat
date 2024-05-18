@echo off
REM Installiere erforderliche Python-Module für das Skript

REM Installiere mysql-connector-python
pip install mysql-connector-python

REM Installiere configparser
pip install configparser

REM Installiere requests
pip install requests

REM Gib eine Meldung aus, wenn die Installation abgeschlossen ist
echo Erforderliche Python-Module wurden installiert.

REM Überprüfe, ob der Ordner "backups" vorhanden ist. Wenn nicht, erstelle den Ordner.
if not exist "%~dp0backups" (
    mkdir "%~dp0backups"
    echo Ordner "backups" wurde erstellt.
) else (
    echo Ordner "backups" ist bereits vorhanden.
)

REM Starte das Python-Skript
cd /d "%~dp0"
python backup_script.py

REM Warte auf Benutzerinteraktion, bevor das Fenster geschlossen wird
pause

REM Warte 5 Sekunden, damit der Benutzer die Nachricht sehen kann, bevor das Fenster geschlossen wird
timeout /t 5 >nul
