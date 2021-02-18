import threading
import sqlite3


class ThreadAgents(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.data = list()  # data for each column in the sqlite database

    def StoreData(self, column, condb):
        con = sqlite3.connect('SQLite_Python.db')
        cursorObj = con.cursor()
        con.cursor()
        sel = 'SELECT {0} FROM {1} WHERE {0} == "{0}"'.format(column, condb)
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()
        for row in rows:
            self.data.append(float(row[0]))
            #print("%s processing %s" % (self.name, float(row[0]))) #if I uncomment these two lines, I can see which
                                                                    #thread is getting what data first.
            #time.sleep(1)

    def run(self):
        print("Starting " + self.name)
        self.StoreData(self.name, self.q)
        print("Exiting " + self.name)

