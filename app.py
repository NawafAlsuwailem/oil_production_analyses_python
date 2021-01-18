from flask import Flask
import json
from service.web_scraper import MyScraper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
myScraper = MyScraper()


@app.route('/')
def hello_world():
    data = myScraper.scrap()

    results = json.dumps(data.fetchall())
    return results


if __name__ == '__main__':
    app.run()
