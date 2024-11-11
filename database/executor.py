#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       


import sqlite3

connection = sqlite3.connect('database/database.sqlite')

cursor = connection.cursor()

def create_table_users() -> None:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            username TEXT,
            since TEXT
        );
    ''')
    connection.commit()

def delete_table(name: str) -> None:
    cursor.execute(f'DROP TABLE IF EXISTS {name}')
    connection.commit()

class User:
    def __init__(self) -> None:
        pass

    def add(id: int, name: str, time: str) -> None:
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (id,))
        existing_user = cursor.fetchone()

        if existing_user:
            return

        cursor.execute('''
            INSERT INTO users (user_id, username, since) VALUES (?, ?, ?)
        ''', (id, name, time))
        connection.commit()

    def remove(id: int) -> None:
        cursor.execute("DELETE FROM users WHERE userid = ?", (id,))
        connection.commit()