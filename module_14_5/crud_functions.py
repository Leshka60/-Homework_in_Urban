import sqlite3


connection = sqlite3.connect('products.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL);
''')

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#                    (f'Продукт{i}', f'Описание{i}', f'{i * 100}'))
#     connection.commit()


def get_all_product():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


connection = sqlite3.connect('registration.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL);
''')


def add_user(username, email, age):
    connection = sqlite3.connect('registration.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', f'{1000}'))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('registration.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True


connection.commit()
connection.close()