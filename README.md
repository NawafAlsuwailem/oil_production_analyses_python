# KAPSARC Test - Backend (Flask)

## problem statment 
The oil-production data includes a number of parameters, which are irreleavant to the end-user. Moreover, many of the given parameters can be discarded to create a clearer view for the oil Export. In addition, the current data shape is driven by the stated information, however, having a few dimensions opens up a better data shape option such as the following:
country | month-year | value

## design
The application should have the three main component: Database, Backend, and Frontend. 
(DB) => The database will be used to store the data in its new format and shape. 
(Backend) => The backend will connect to the data source, data target and frontend. In addition to its functionality as a data wrangling unit.
(Frontend) => The front will display the new table along with charts reflecting data stats

## solution - implementation 
(DB) => the database was developed with Sqlite 3 and it consist of tables: oil_export (original data), oil_export_avg (for average export for each country), and oil_export_mont_total (for the total of exports per month)
(Backend) => backend was developed with Python3 & Flask. It connects to the data source, scrape the data, transform, store and expose via APIs
(Frontend) => finall, the frontend was developed with Angular 8 & bootstrap. It connects to the backend APIs and display the data in tables, and charts

## dependencies
(DB) => none

(Backend)
- BeautifulSoup
- seleniumwire
- selenium
- sqlite3
- Flask
- CORS

(Frontend) 
- Angular 8
- Bootstrap 4

## API
(Backend)
get data => /
get average => /export_avg
get total => /month_sum

(Frontend)
dashboard => /
