#!/bin/bash

# Installiere erforderliche Python-Module für das Skript

# Installiere mysql-connector-python
pip install mysql-connector-python

# Installiere configparser
pip install configparser

# Installiere requests
pip install requests

# Gib eine Meldung aus, wenn die Installation abgeschlossen ist
echo "Erforderliche Python-Module wurden installiert."

# Starte das Python-Skript
cd "$(dirname "$0")"
python3 backup_script.py

# Warte auf Benutzerinteraktion, bevor das Fenster geschlossen wird
read -p "Drücken Sie eine beliebige Taste zum Fortfahren ..."

# Warte 5 Sekunden, damit der Benutzer die Nachricht sehen kann, bevor das Fenster geschlossen wird
sleep 5
