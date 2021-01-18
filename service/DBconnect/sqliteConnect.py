import sqlite3
from model.oilExport import OilExport


class SqliteConnect:
    def __init__(self):
        self.dataList = []
        self.conn = sqlite3.connect('kapsarc_test.db', check_same_thread=False)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS oil_export (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          country VARCHAR(100) NOT NULL,
          export_date DATETIME NOT NULL,
          val FLOAT NOT NULL);
        ''')
        self.conn.commit()

    def retrieveData(self):
        query = "SELECT * FROM oil_export"
        return self.conn.execute(query)

    def getDBsize(self):
        query = "SELECT COUNT(*) FROM oil_export"
        result = self.conn.execute(query)
        size = result.fetchall().pop()[0]
        return size

    def insertRecord(self, data):
        query = "INSERT INTO oil_export (country,export_date,val) VALUES (?,?,?)"
        self.conn.execute(query, data)
        self.conn.commit()

    def updateRecordById(self, data):
        query = "UPDATE oil_export SET country=?, export_date=?, val=? WHERE id=?"
        self.conn.execute(query, data)
        self.conn.commit()

    def deleteRecordById(self, idd):
        query = "DELETE FROM oil_export WHERE id=?"
        self.conn.execute(query, (idd,))
        self.conn.commit()

    def getDataAsList(self):
        results = self.retrieveData()
        oilExports = results.fetchall()
        return oilExports

    def exit(self):
        self.conn.close()
