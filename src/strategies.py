# Date and web scraper imports
import datetime
import web_scraper

# Constants
AVERAGE_CLOSING_PRICE = 'Average Closing Price'
YEARLY_PAYOUT = 1.00
TOTAL_YEARS = 100

# Data Types
CURRENT_HIGH_FUTURE_HIGH = 'Current High Future High'
CURRENT_HIGH_FUTURE_LOW = 'Current High Future Low'
CURRENT_LOW_FUTURE_HIGH = 'Current Low Future High'
CURRENT_LOW_FUTURE_LOW = 'Current Low Future Low'

# Declaring current year and first year
CURRENT_YEAR = datetime.datetime.now().year
FIRST_YEAR = CURRENT_YEAR - TOTAL_YEARS

# Get data from web scraper
data = web_scraper.get_data()

# Instantly invest every dollar
def every_dollar():
	shares = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		shares += YEARLY_PAYOUT / data[year][AVERAGE_CLOSING_PRICE]
	return shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest a single dollar anytime the market is not at an all time high
def single_dollar_not_at_high():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
		else:
			cash -= YEARLY_PAYOUT
			shares += YEARLY_PAYOUT / share_price
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest half of cash anytime the market is not at an all time high
def half_cash_not_at_high():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
		else:
			cash /= 2.0
			shares += cash / share_price
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest all cash anytime the market is not at an all time high
def all_cash_not_at_high():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
		else:
			shares += cash / share_price
			cash = 0.0
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest or sell a single dollar depending on if the market is at an all time high
def single_dollar_buy_and_sell():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
			if shares > YEARLY_PAYOUT / share_price:
				shares -= YEARLY_PAYOUT / share_price
				cash += YEARLY_PAYOUT
			elif shares > 0:
				cash += shares * share_price
				shares = 0
		else:
			cash -= YEARLY_PAYOUT
			shares += YEARLY_PAYOUT / share_price
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest or sell half of cash depending on if the market is at an all time high
def half_cash_buy_and_sell():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
			if shares > 0:
				shares /= 2.0
				cash += shares * share_price
		else:
			cash /= 2.0
			shares += cash / share_price
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Invest or sell all cash depending on if the market is at an all time high
def all_cash_buy_and_sell():
	cash = 0.0
	shares = 0.0
	all_time_high = 0.0
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		cash += YEARLY_PAYOUT
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
			if shares > 0:
				cash += shares * share_price
				shares = 0
		else:
			shares += cash / share_price
			cash = 0.0
	return cash + shares * data[CURRENT_YEAR][AVERAGE_CLOSING_PRICE]

# Comparing past highs vs future lows
def past_high_vs_future_low():
	past_high = []
	future_low = []
	all_time_high = 0.0
	all_time_low = float('inf')
	data_types = {
		CURRENT_HIGH_FUTURE_HIGH: 0,
		CURRENT_HIGH_FUTURE_LOW: 0,
		CURRENT_LOW_FUTURE_HIGH: 0,
		CURRENT_LOW_FUTURE_LOW: 0
	}
	for year in range(FIRST_YEAR, CURRENT_YEAR):
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_high < share_price:
			all_time_high = share_price
			past_high.append(True)
		else:
			past_high.append(False)
	for year in reversed(range(FIRST_YEAR, CURRENT_YEAR)):
		share_price = data[year][AVERAGE_CLOSING_PRICE]
		if all_time_low > share_price:
			all_time_low = share_price
			future_low.insert(0, True)
		else:
			future_low.insert(0, False)
	for index in range(TOTAL_YEARS):
		if past_high[index]:
			if future_low[index]:
				data_types[CURRENT_HIGH_FUTURE_LOW] += 1
			else:
				data_types[CURRENT_HIGH_FUTURE_HIGH] += 1
		else:
			if future_low[index]:
				data_types[CURRENT_LOW_FUTURE_LOW] += 1
			else:
				data_types[CURRENT_LOW_FUTURE_HIGH] += 1
	#return data_types
	return [past_high, future_low]
