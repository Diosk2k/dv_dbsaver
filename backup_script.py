import os
import mysql.connector
import subprocess
import datetime
import configparser
import time
import requests
import json
from custom_locale import locales

def print_start_animation():
    logo = r"""

   ___ _   __  ________    __     _______ _   _________ 
  / _ \ | / / / __/ __ \  / /    / __/ _ | | / / __/ _ \
 / // / |/ / _\ \/ /_/ / / /__  _\ \/ __ | |/ / _// , _/
/____/|___/ /___/\___\_\/____/ /___/_/ |_|___/___/_/|_| 
                                                        

    """
    print(logo)
    loading = "DV DEV"
    print(loading)
    for i in range(3):
        for char in "-\\|/":
            print(f"\r{loading} {char}", end="")
            time.sleep(0.2)
    print("\r" + " " * len(loading) + " " * 4, end="\r")  # Clear the line

def backup_database(host, username, password, database_name, backup_folder, dump_path, language, webhook_enable, webhook_url, embed_settings):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if not backup_folder:
            backup_folder = os.path.join(script_dir, 'backups')

        # Make sure backup folder exists
        os.makedirs(backup_folder, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = os.path.join(backup_folder, f"mysql_backup_{database_name}_{timestamp}.sql")

        # Using --defaults-extra-file to handle passwords securely
        password_file = os.path.join(script_dir, "mysql_password.cnf")
        with open(password_file, 'w') as f:
            f.write(f"[client]\nuser={username}\npassword={password}\nhost={host}\n")

        command = f"{dump_path} --defaults-extra-file={password_file} {database_name} > {backup_file}"
        subprocess.run(command, shell=True, check=True)

        os.remove(password_file)  # Clean up password file

        message = locales[language]["backup_success"].format(database_name=database_name)
        if webhook_enable:
            send_discord_webhook(message, webhook_url, backup_file, embed_settings, language)

        print(f"Sicherungsdatei erstellt: {backup_file}")
    except subprocess.CalledProcessError as e:
        message = locales[language]["backup_error"].format(database_name=database_name, error=e)
        if webhook_enable:
            send_discord_webhook(message, webhook_url, backup_file, embed_settings, language)

def send_discord_webhook(message, webhook_url, backup_file, embed_settings, language):
    embed = {
        'content': message,
        'embeds': [{
            'title': embed_settings.get("title", locales[language]["embed_settings"]["title"]),
            'description': embed_settings.get("description", locales[language]["embed_settings"]["description"]),
            'color': embed_settings.get("color", locales[language]["embed_settings"]["color"]),
            'fields': [
                {'name': 'Datei', 'value': backup_file}
            ],
            'author': {
                'name': embed_settings.get("author_name", locales[language]["embed_settings"]["author_name"]),
                'icon_url': embed_settings.get("author_icon_url", locales[language]["embed_settings"]["author_icon_url"])
            }
        }]
    }

    files = {'file': open(backup_file, 'rb')}
    response = requests.post(webhook_url, files=files, data={'payload_json': json.dumps(embed)})
    if response.status_code != 200:
        print(f"Failed to send Discord webhook: {response.text}")

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    if not all(section in config for section in ["DATABASE", "LOCALE", "WEBHOOK", "EMBEDDING"]):
        raise ValueError("Config file must contain sections DATABASE, LOCALE, WEBHOOK, and EMBEDDING")
    return config["DATABASE"], config["LOCALE"], config["WEBHOOK"], config["EMBEDDING"]

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, "config.ini")
    database_config, locale_config, webhook_config, embedding_config = read_config(config_file)

    host = database_config.get("host")
    username = database_config.get("username")
    password = database_config.get("password")
    database_name = database_config.get("database_name")
    backup_folder = database_config.get("backup_folder", "")
    backup_interval = int(database_config.get("backup_interval", 3600))
    dump_path = database_config.get("dump_path", "C:/xampp/mysql/bin/mysqldump")  # Standardpfad, falls nicht in der Konfiguration angegeben
    language = locale_config.get("language", "de")
    webhook_enable = webhook_config.getboolean("enable", False)
    webhook_url = webhook_config.get("url")

    embed_settings = {}
    if "EMBEDDING" in embedding_config:
        embed_settings = embedding_config["EMBEDDING"]

    if language not in locales:
        print(f"Warning: Language '{language}' is not supported. Default is English.")
        language = "en"

    print_start_animation()
    print("Database backup is running...")

    while True:
        backup_database(host, username, password, database_name, backup_folder, dump_path, language, webhook_enable, webhook_url, embed_settings)
        print(locales[language]["next_backup"].format(backup_interval=backup_interval))
        time.sleep(backup_interval)

if __name__ == "__main__":
    main()
