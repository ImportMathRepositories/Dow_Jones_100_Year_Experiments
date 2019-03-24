import strategies

# Formats
DOLLAR_FORMAT = '${:,.2f}'
PERCENT_FORMAT = '{:,.2f}%'

# Data Types
CURRENT_HIGH_FUTURE_HIGH = 'Current High Future High'
CURRENT_HIGH_FUTURE_LOW = 'Current High Future Low'
CURRENT_LOW_FUTURE_HIGH = 'Current Low Future High'
CURRENT_LOW_FUTURE_LOW = 'Current Low Future Low'

def print_as_dollar(x):
	print(DOLLAR_FORMAT.format(x))

def print_as_percent(x):
	print(PERCENT_FORMAT.format(100.0 * x))

print('\nDow Jones: 100 years with an income of $1 per year\n')

print('Instantly invest every dollar:')
print_as_dollar(strategies.every_dollar())
print('Invest a single dollar anytime the market is not at an all time high:')
print_as_dollar(strategies.single_dollar_not_at_high())
print('Invest half of cash anytime the market is not at an all time high')
print_as_dollar(strategies.half_cash_not_at_high())
print('Invest all cash anytime the market is not at an all time high')
print_as_dollar(strategies.all_cash_not_at_high())
print('Invest or sell a single dollar depending on if the market is at an all time high')
print_as_dollar(strategies.single_dollar_buy_and_sell())
print('Invest or sell half of cash depending on if the market is at an all time high')
print_as_dollar(strategies.half_cash_buy_and_sell())
print('Invest or sell all cash depending on if the market is at an all time high')
print_as_dollar(strategies.all_cash_buy_and_sell())

data_types = strategies.past_high_vs_future_low()

print('All time high and future all time low:')
print_as_percent(1.0 * data_types[CURRENT_HIGH_FUTURE_LOW] / (data_types[CURRENT_HIGH_FUTURE_LOW] + data_types[CURRENT_HIGH_FUTURE_HIGH]))
print('Relative low and future all time low:')
print_as_percent(1.0 * data_types[CURRENT_LOW_FUTURE_LOW] / (data_types[CURRENT_LOW_FUTURE_LOW] + data_types[CURRENT_LOW_FUTURE_HIGH]))
