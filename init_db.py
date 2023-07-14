"""
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sqlite3') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
"""
