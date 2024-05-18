# Backup Script

## Description
This script automates the installation of required Python modules and executes a Python script for backup purposes. It checks for the existence of a "backups" folder and creates it if necessary. After installing the required modules and creating the folder, it starts the backup script.

## Requirements
- Python 3
- pip package manager

## Configuration
The script can be configured via the `config.ini` file located in the same directory as the script. Here are the configurable options:

### DATABASE
- `host`: Hostname of the database server.
- `username`: Username to access the database.
- `password`: Password to access the database.
- `database_name`: Name of the database to be backed up.
- `backup_interval`: Interval (in seconds) between each backup operation.
- `dump_path`: Path to the `mysqldump` executable. (Example: `C:/xampp/mysql/bin/mysqldump`)

### LOCALE
- `language`: Language setting. Currently available languages are:
  - `de` for German
  - `en` for English
  - `es` for Spanish
  - `zh` for Chinese
  - `hi` for Hindi
  - `fr` for French


### WEBHOOK
- `enable`: Whether to enable webhook notifications. (Options: `true` or `false`)
- `url`: URL of the webhook.

### EMBEDDING
- `author_icon_url`: URL of the author icon for webhook messages.

## Custom Locales
To create custom locales, you can modify the `custom_locale.py` file. This file contains a dictionary named `locales` with language codes as keys and corresponding translation dictionaries as values. You can add new languages or modify existing translations as needed.

## Author
- [@Diosk](https://github.com/Diosk2k)

## Need Help?
For assistance or questions, please join our Discord server.


