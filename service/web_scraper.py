import time
from bs4 import BeautifulSoup
from seleniumwire import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from service.DBconnect.sqliteConnect import SqliteConnect
from selenium.webdriver.common.keys import Keys


class MyScraper:

    def __init__(self, headless=True):
        self.db = SqliteConnect()
        self.chromedriver = "service/chromedriver"
        self.browser = None
        self.headless = headless

    def startBrowser(self):
        profile = webdriver.ChromeOptions()
        profile.add_argument('--no-sandbox')
        profile.add_experimental_option('excludeSwitches', ['enable-automation'])
        if self.headless: profile.add_argument('--headless')

        self.browser = webdriver.Chrome(executable_path=self.chromedriver, options=profile)
        self.browser.set_page_load_timeout(180)
        self.browser.set_window_size(1800, 1020)

    def scrap(self):
        if int(self.db.getDBsize()) < 1755:
            # init browser
            self.startBrowser()
            wait = ui.WebDriverWait(self.browser, 180)
            # scrap data
            self.browser.get("http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906")
            wait.until(EC.visibility_of_element_located((By.ID, "DataTable")))
            self.browser.execute_script("selectItem(2,3);")
            time.sleep(2)
            html = self.browser.find_element_by_tag_name('html')
            html.send_keys(Keys.END)
            time.sleep(3)

            legit = 0
            for req in self.browser.requests:
                if req.response and req.url.find("getData.aspx") >= 0:
                    legit += 1
                    if legit >= 2:
                        respData = req.response.body.decode("utf-8")

                        soup = BeautifulSoup(respData, "html.parser")
                        months = soup.find_all("collabel")

                        for row in soup.find_all("row"):
                            country = row.find("rowlabel").text
                            vals = row.find_all("c")

                            for i, val in enumerate(vals):
                                self.db.insertRecord((country, months[i].text, val["f"]))

            self.browserExit()
        self.db.generateExportAvg()
        self.db.generateExportTotal()
        return self.db.retrieveData()


    def browserExit(self):
        self.browser.quit()

