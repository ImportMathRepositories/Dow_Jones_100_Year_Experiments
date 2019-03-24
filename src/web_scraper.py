# Web scraping imports
import bs4
import urllib2

# Dow Jones 100 year chart data url
URL = 'https://www.macrotrends.net/1319/dow-jones-100-year-historical-chart'

# XML parsing argument
LXML = 'lxml'

# ID of the div containing the data
STYLE_1 = 'style-1'

# HTML tags and keywords
DIV = 'div'
TABLE = 'table'
TBODY = 'tbody'
TR = 'tr'
TD = 'td'
ID = 'id'

# Dictionary keys
AVERAGE_CLOSING_PRICE = 'Average Closing Price'
YEAR_OPEN = 'Year Open'
YEAR_HIGH = 'Year High'
YEAR_LOW = 'Year Low'
YEAR_CLOSE = 'Year Close'
ANNUAL_CHANGE = 'Annual Change'

def get_data():
	year_dict = {}
	html = urllib2.urlopen(URL)
	soup = bs4.BeautifulSoup(html, LXML)

	div = soup.find(DIV, {ID: STYLE_1})
	table = div.find_all(TABLE)[0]
	tbody = table.find_all(TBODY)[0]
	rows = tbody.find_all(TR)

	for row in rows:
		current_year = {}
		tds = row.find_all(TD)

		current_year[AVERAGE_CLOSING_PRICE] = float(tds[1].getText().replace(',', ''))
		current_year[YEAR_OPEN] = float(tds[2].getText().replace(',', ''))
		current_year[YEAR_HIGH] = float(tds[3].getText().replace(',', ''))
		current_year[YEAR_LOW] = float(tds[4].getText().replace(',', ''))
		current_year[YEAR_CLOSE] = float(tds[5].getText().replace(',', ''))
		current_year[ANNUAL_CHANGE] = float(tds[6].getText().strip('%'))

		year_dict[int(tds[0].getText())] = current_year

	return year_dict
