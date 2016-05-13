#!/usr/local/bin/python3.4

# adapted from
# http://codereview.stackexchange.com/questions/78643/create-sqlite-backups

# TODO: extend manage.py to make this a command

import sqlite3
import shutil
import time
import os

NO_OF_DAYS = 15 # keep data for 15 days
DB_FILE    = "db.sqlite3"
BACKUP_DIR = "veganizzm/backups"

def sqlite3_backup():
    parts = os.path.splitext(DB_FILE)
    backup_file = os.path.join(
        BACKUP_DIR, parts[0] +
        time.strftime('_%Y-%m-%d_%H%M%S') + parts[1]
    )

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('begin immediate')
    shutil.copyfile(DB_FILE, backup_file)
    connection.rollback()
    connection.close()

def clean():
    for filename in os.listdir(BACKUP_DIR):
        backup_file = os.path.join(BACKUP_DIR, filename)
        if os.stat(backup_file).st_ctime < (time.time() - NO_OF_DAYS * 86400):
            if os.path.isfile(backup_file):
                os.remove(backup_file)

if __name__ == "__main__":
    if not os.path.isdir(BACKUP_DIR):
        raise Exception("Backup directory does not exist: {}".format(BACKUP_DIR))
    
    sqlite3_backup()
    clean()
