#!/bin/bash

pip install mysql-connector-python

pip install configparser

pip install requests

echo "Required Python modules have been installed."

if [ ! -d "backups" ]; then
    mkdir backups
    echo "Folder 'backups' has been created."
else
    echo "Folder 'backups' already exists."
fi

python3 backup_script.py

read -p "Press Enter to continue..."

sleep 5
