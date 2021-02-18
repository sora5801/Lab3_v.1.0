import sqlite3
import requests
from bs4 import BeautifulSoup
from WebScraper import WebScraper


class SQLdatabase:
        def __init__(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Database created and Successfully Connected to SQLite")
                sqlite_select_Query = "select sqlite_version();"
                cursor.execute(sqlite_select_Query)
                record = cursor.fetchall()
                print("SQLite Database Version is: ", record)
                cursor.close()

            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    #print("The SQLite connection is closed")


        def Fetch(self,column, condb):
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursorObj = self.sqliteConnection.cursor()
            self.sqliteConnection.cursor()
            sel = 'SELECT {0} FROM {1} WHERE {0} == "{0}"'.format(column, condb)
            cursorObj.execute(sel)
            rows = cursorObj.fetchall()
            return rows

        def Table(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = '''CREATE TABLE Database (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            photo text NOT NULL UNIQUE,
                                            html text NOT NULL UNIQUE);'''

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                print("SQLite table created")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)
            finally:
                if (self.sqliteConnection):
                    self.sqliteConnection.close()
                    #print("sqlite connection is closed")


        def readSqliteTable(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_select_query = """SELECT * from Database"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                print("Printing each row")
                for row in records:
                    print("id: ", row[0])
                    print("name: ", row[1])
                    print("photo: ", row[2])
                    print("html: ", row[3])
                    print("\n")

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("The SQLite connection is closed")



        def deleteRecord(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                # Deleting single record now
                sql_delete_query = """DELETE from Database where id = 2"""
                cursor.execute(sql_delete_query)
                self.sqliteConnection.commit()
                print("Record deleted successfully ")
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to delete record from sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("the sqlite connection is closed")

        def convertToBinaryData(self,filename):
            # Convert digital data to binary format
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData

        def insertBLOB(self,empId, name, photo, resumeFile):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")
                sqlite_insert_blob_query = """ INSERT INTO Database
                                          (id, name, photo, html) VALUES (?, ?, ?, ?)"""

                empPhoto = self.convertToBinaryData(photo)
                resume = self.convertToBinaryData(resumeFile)
                # Convert data into tuple format
                data_tuple = (empId, name, empPhoto, resume)
                cursor.execute(sqlite_insert_blob_query, data_tuple)
                self.sqliteConnection.commit()
                print("Image and file inserted successfully as a BLOB into a table")
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to insert blob data into sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("the sqlite connection is closed")

        def updateSqliteTable(self,id, htext):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update Database set html = ? where id = ?"""
                data = (htext, id)
                cursor.execute(sql_update_query, data)
                self.sqliteConnection.commit()
                print("Record Updated successfully")
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to update sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("The sqlite connection is closed")

        def DeleteDatabase(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = """DROP TABLE Database"""

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                print("Database deleted")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while deleting database", error)

            finally:
                if self.sqliteConnection:
                   self.sqliteConnection.close()
                   print("sqlite connection is closed")

        def soupDatabase(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Soup (
                                                        id INTEGER PRIMARY KEY,
                                                        soup text NOT NULL );'''

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                #print("SQLite table created")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)

            finally:
                if self.sqliteConnection:
                   self.sqliteConnection.close()
                  # print("sqlite connection is closed")

        def insertSoup(self,id, soup):

            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                #  print("Connected to SQLite")
                sqlite_insert_blob_query = """ INSERT INTO Soup
                                                            (id, soup) VALUES (?, ?)"""
                data_tuple = (id, soup)
                cursor.execute(sqlite_insert_blob_query, data_tuple)
                self.sqliteConnection.commit()
                #  print("Temperature datas successfully inserted into the Temperature table")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert temperature data into sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                #  print("the sqlite connection is closed")

        def readSoup(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_select_query = """SELECT * from Soup"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchone()
                return records[1]

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("The SQLite connection is closed")

        def GRFDatabase(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = '''CREATE TABLE GRF (
                                                        year INTEGER PRIMARY KEY,
                                                        CO2 REAL NOT NULL,
                                                        CH4 REAL NOT NULL ,
                                                        N2O REAL NOT NULL,
                                                        CFC12 REAL NOT NULL,
                                                        CFC11 REAL NOT NULL,
                                                        n15minor REAL NOT NULL);''' #n was added because sql does
                #not allow columns names to start with numbers.Also the dash was remove because of a syntax error

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                #print("SQLite table created")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)

            finally:
                if self.sqliteConnection:
                   self.sqliteConnection.close()
                  # print("sqlite connection is closed")

        def readGRFTable(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_select_query = """SELECT * from GRF"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                print("Printing each row")
                for row in records:
                    print("Year: ", row[0])
                    print("CO2: ", row[1])
                    print("CH4: ", row[2])
                    print("N2O: ", row[3])
                    print("CFC12: ", row[4])
                    print("CFC11: ", row[5])
                    print("15-minor: ", row[6])
                    print("\n")

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("The SQLite connection is closed")

        def insertGRFData(self):
            WS = WebScraper()
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
              #  print("Connected to SQLite")
                sqlite_insert_blob_query = """ INSERT INTO GRF
                                                      (year, CO2, CH4, N2O, CFC12, CFC11, n15minor) 
                                                      VALUES (?, ?, ?, ?, ?, ?, ?)"""
                '''
                URL = 'https://www.esrl.noaa.gov/gmd/aggi/aggi.html'  # The url to get info
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                table = soup.findAll('table')[1]
                table_rows = table.find_all("tr")
                for tr in table_rows[4:]:
                    td = tr.find_all('td')
                    row = [i.text for i in td]
                    data_tuple = (int(row[0]), row[1],
                                  row[2], row[3], row[4],row[5],row[6])
                '''
                for i in WS.data:
                    data_tuple = (i[0], i[1],
                                  i[2], i[3], i[4], i[5], i[6])
                    cursor.execute(sqlite_insert_blob_query, data_tuple)
                self.sqliteConnection.commit()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert GRF data into sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                  #  print("the sqlite connection is closed")

        def DeleteGRF(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = """DROP TABLE GRF"""

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                print("Database deleted")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while deleting database", error)

            finally:
                if self.sqliteConnection:
                   self.sqliteConnection.close()
                   print("sqlite connection is closed")
