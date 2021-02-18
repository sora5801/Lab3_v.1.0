from SQLdatabase import SQLdatabase
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from Thread import ThreadAgents
import sqlite3

class BackEnd:
    def __init__(self):
        self.SQ = SQLdatabase()
        con = sqlite3.connect('SQLite_Python.db')
        cursorObj = con.cursor()
        con.cursor()
        sel = 'SELECT year FROM GRF WHERE year == "year"'
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()
        c= con.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='GRF' ''')
        if c.fetchone()[0] != 1:
            self.SQ.GRFDatabase()
            self.SQ.insertGRFData()
        self.years = rows
        self.threadCO2 = ThreadAgents("CO2", 'GRF')
        self.threadCH4 = ThreadAgents("CH4", 'GRF')
        self.threadN2O = ThreadAgents("N2O", 'GRF')
        self.threadCFC12 = ThreadAgents("CFC12", 'GRF')
        self.threadCFC11 = ThreadAgents("CFC11", 'GRF')
        self.thread15minor = ThreadAgents("n15minor", 'GRF')
        self.threadCO2.start()
        # threadCO2.join()
        self.threadCH4.start()
        # threadCH4.join()
        self.threadN2O.start()
        # threadN2O.join()
        self.threadCFC12.start()
        # threadCFC12.join()
        self.threadCFC11.start()
        # threadCFC11.join()
        self.thread15minor.start()
        # thread15minor.join()
        self.threadCO2.join()
        self.threadCH4.join()
        self.threadN2O.join()
        self.threadCFC12.join()
        self.threadCFC11.join()
        self.thread15minor.join()
        self.CO2 = self.threadCO2.data
        self.CH4 = self.threadCH4.data
        self.N2O = self.threadN2O.data
        self.CFC12 = self.threadCFC12.data
        self.CFC11 = self.threadCFC11.data
        self.n15minor = self.thread15minor.data

    def LinearRegression(self):
        a1 = np.array(self.years).reshape(-1, 1)
        c1 = np.array(self.threadCO2.data)
        plt.figure(1, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a1, c1)  # perform linear regression
        Y_pred = linear_regressor.predict(a1)  # make predictions
        plt.scatter(a1, c1)
        plt.ylabel("CO2")
        plt.xlabel("Years")
        plt.title("CO2 vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a1, Y_pred, color='red')

        a2 = np.array(self.years).reshape(-1, 1)
        c2 = np.array(self.threadCO2.data)
        plt.figure(2, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a2, c2)  # perform linear regression
        Y_pred2 = linear_regressor.predict(a2)  # make predictions
        plt.scatter(a2, c2)
        plt.ylabel("CH4")
        plt.xlabel("Years")
        plt.title("CH4 vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a2, Y_pred2, color='red')

        a3 = np.array(self.years).reshape(-1, 1)
        c3 = np.array(self.threadN2O.data)
        plt.figure(3, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a3, c3)  # perform linear regression
        Y_pred3 = linear_regressor.predict(a3)  # make predictions
        plt.scatter(a3, c3)
        plt.ylabel("N2O")
        plt.xlabel("Years")
        plt.title("N2O vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a2, Y_pred3, color='red')

        a4 = np.array(self.years).reshape(-1, 1)
        c4 = np.array(self.threadCFC12.data)
        plt.figure(4, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a4, c4)  # perform linear regression
        Y_pred4 = linear_regressor.predict(a4)  # make predictions
        plt.scatter(a4, c4)
        plt.ylabel("CFC12")
        plt.xlabel("Years")
        plt.title("CFC12 vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a2, Y_pred4, color='red')

        a5 = np.array(self.years).reshape(-1, 1)
        c5 = np.array(self.threadCFC11.data)
        plt.figure(5, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a2, c2)  # perform linear regression
        Y_pred5 = linear_regressor.predict(a2)  # make predictions
        plt.scatter(a2, c2)
        plt.ylabel("CFC11")
        plt.xlabel("Years")
        plt.title("CFC11 vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a2, Y_pred5, color='red')

        a6 = np.array(self.years).reshape(-1, 1)
        c6 = np.array(self.thread15minor.data)
        plt.figure(6, figsize=(7, 5))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a2, c2)  # perform linear regression
        Y_pred6 = linear_regressor.predict(a2)  # make predictions
        plt.scatter(a2, c2)
        plt.ylabel("15-minor")
        plt.xlabel("Years")
        plt.title("15-minor vs years Linear Regression")
        # plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a2, Y_pred6, color='red')

        plt.show()



