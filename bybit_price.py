import requests


def get_bybit_prices(symbols):
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)

    prices = {}

    if response.status_code == 200:
        data = response.json()
        for ticker in data['result']:
            symbol = ticker['symbol']
            if symbol in symbols:
                prices[symbol] = ticker['last_price']
    else:
        for symbol in symbols:
            prices[symbol] = None

    return prices


# Define the symbols you want to fetch prices for
# Note: Bybit uses different symbol formats, e.g., BTCUSD for BTC/USD
symbols = ['BTCUSD', 'ETHUSD', 'AAVEUSD', 'UNIUSD', 'LINKUSD']

# Get the prices
prices = get_bybit_prices(symbols)

# Print the prices
for symbol, price in prices.items():
    if price:
        print(f"The current price of {symbol} is ${price}")
    else:
        print(f"Failed to fetch the price for {symbol}")





