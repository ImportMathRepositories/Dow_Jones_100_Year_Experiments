# Dow\_Jones\_100\_Year\_Experiments
Performance comparison between different investing strategies over the past 100 years of the Dow Jones

# Disclaimers and Warnings:
+ Never use a web scraper for purposes outside of normal website use (at risk of having your IP blocked).
+ I have no affiliation with the website that I am scraping in this repository, but I doubt anyone will have a problem with its use.
+ Scraping is a product of the current state of a website and can easily become outdated/broken upon the update of a website.
+ Link to free Dow Jones market data source: https://www.macrotrends.net/1319/dow-jones-100-year-historical-chart

# Running this code on your machine:
1. Have a functioning Python 2.7+ version installed
2. Make sure that Beautiful Soup is installed and working properly (urllib2, bs4, and lxml are all needed)
3. Clone this repository
4. Open a terminal and cd into src
5. Run this command: "python main.py"

# Explanation of the Code:
+ All of the data is scraped using the Beautiful Soup library in web_scraper.py
+ Seven different investing strategies are performed via seven different functions in strategies.py
+ This file also has one additional function for comparing past highs and future lows
+ The final file (main.py) simply calls and prints the results in a logical fashion
