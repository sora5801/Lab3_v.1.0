from bs4 import BeautifulSoup
import re
import json
import sqlite3
import threading
'''
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
'''
Presidents = {}
def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)


with open("Presidents.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, features ='lxml')
    for b in soup.find_all('b'):
        if hasNumbers(b.text) == True:
            x = re.search("\d+", b.text)
            Presidents[int(x.group())] = ""
    for a ,b  in zip(soup.find_all('a'), Presidents.keys()):
        Presidents[b] = a.text

def PrintIt(t):
    print(type(t))
    print(json.dumps(t))
    print(type(json.dumps(t)))
    print('----------')

p = json.dumps(Presidents)
print(p)


def insertJSON(id, json):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        #  print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO Soup
                                                    (id, soup) VALUES (?, ?)"""
        data_tuple = (id, json)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert temperature data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
        #  print("the sqlite connection is closed")
'''
class TimeThread (threading.Thread):
    def __init__(self, id, json):
        threading.Thread.__init__(self)
        self.id = id
        self.json = json
    def run(self):
        print("Starting " + self.name)
        insertJSON(self.id, self.json)
        print("Exiting " + self.name)

TimeThread(1, p)
'''
'''
data = readfromstring(p)
f = open("Presidents.xml", "w")
f.write(json2xml.Json2xml(data).to_xml())
'''


class TimeThread(threading.Thread):
    def __init__(self, target, *args):
        self.target = target
        self.args = args
        threading.Thread.__init__(self)

    def run(self):
        print("Starting " + self.name)
        self.target(*self.args)
        print("Exiting " + self.name)


t1 = TimeThread(insertJSON, 2, p)
t1.start()
t1.join()







