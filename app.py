from flask import Flask
import json
from service.web_scraper import WebScrapper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
myScraper = WebScrapper()


@app.route('/')
def getOilExports():
    data = myScraper.scrap()
    results = json.dumps(data.fetchall())
    return results


if __name__ == '__main__':
    app.run()
