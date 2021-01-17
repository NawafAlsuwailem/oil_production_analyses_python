from flask import Flask
import json
from service.web_scraper import MyScraper
from service.DBconnect.sqliteConnect import SqliteConnect

app = Flask(__name__)

sqlConnect = SqliteConnect()
myScraper = MyScraper()

@app.route('/')
def hello_world():
    sqlConnect.getDataAsList()
    data = myScraper.scrap()
    results = json.dumps(data.fetchall())
    # print(json.dumps(data.fetchall()))
    return results
    # query = "SELECT * FROM oil_export"
    # return myDB.conn.execute(query)
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
