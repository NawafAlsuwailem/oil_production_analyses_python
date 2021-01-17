import sqlite3
from models.oilExport import OilExport
import json

class SqliteConnect:
    def __init__(self):
        self.dataList = []
        self.conn = sqlite3.connect('kapsarc_test.db', check_same_thread=False)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS oil_export (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          country VARCHAR(100) NOT NULL,
          creation_date DATETIME NOT NULL,
          val FLOAT NOT NULL);
        ''')
        self.conn.commit()

        print("Database initialized")

    def insertRecord(self,data): # data is a tuple like (Albania,Sept2020,2321)
        query = "INSERT INTO oil_export (country,creation_date,val) VALUES (?,?,?)"
        self.conn.execute(query,data)
        self.conn.commit()

    def updateRecordById(self,data):
        query = "UPDATE oil_export SET country=?, creation_date=?, val=? WHERE id=?"
        self.conn.execute(query, data)
        self.conn.commit()

    def deleteRecordById(self,idd):
        query = "DELETE FROM oil_export WHERE id=?"
        self.conn.execute(query,(idd,))
        self.conn.commit()

    def retrieveData(self):
        query = "SELECT * FROM oil_export"
        return self.conn.execute(query)

    def displayData(self):
        items = self.retrieveData()
        for item in items:
            print("Country: {0} Date {1} Value {2}".format(item[1], item[2], item[3]))

    # def getDataAsList(self):
    #     items = self.retrieveData()
    #     print(type(items))
    #     for i in items:
    #
    #         print(i)

    def getDBsize(self):
        query = "SELECT COUNT(*) FROM oil_export"
        result = self.conn.execute(query)
        size = result.fetchall().pop()[0]
        return size

    def exit(self):
        self.conn.close()
