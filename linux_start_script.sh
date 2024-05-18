#!/bin/bash

# Install required Python modules for the script
# Install mysql-connector-python
pip install mysql-connector-python

# Install configparser
pip install configparser

# Install requests
pip install requests

# Print a message when installation is completed
echo "Required Python modules have been installed."

# Check if the "backups" folder exists. If not, create the folder.
if [ ! -d "backups" ]; then
    mkdir backups
    echo "Folder 'backups' has been created."
else
    echo "Folder 'backups' already exists."
fi

# Start the Python script
python3 backup_script.py

# Wait for user interaction before closing the window
read -p "Press Enter to continue..."

# Wait for 5 seconds to allow the user to see the message before closing the window
sleep 5
