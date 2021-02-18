import sqlite3
import json


def Fetch(column, condb):
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursorObj = sqliteConnection.cursor()
    sqliteConnection.cursor()
    sel = 'SELECT {0} FROM {1} WHERE {0} == "{0}"'.format(column, condb)
    cursorObj.execute(sel)
    rows = cursorObj.fetchall()
    return rows


def PrintIt(t):
    print(type(t))
    print(json.dumps(t))
    print(type(json.dumps(t)))
    print('----------')


PrintIt(Fetch('CO2', 'GRF'))
PrintIt(Fetch("CH4", 'GRF'))
PrintIt(Fetch("N2O", 'GRF'))
PrintIt(Fetch("CFC12", 'GRF'))
PrintIt(Fetch("CFC11", 'GRF'))
PrintIt(Fetch("n15minor",
              'GRF'))  # supposed to bed 15-minor, but sqlite column does not allow the names to start with a number
