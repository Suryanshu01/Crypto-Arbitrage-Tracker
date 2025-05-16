import requests

def get_binance_us_prices(symbols):
    base_url = "https://api.binance.us/api/v3/ticker/price"
    prices = {}

    try:
        response = requests.get(base_url)
        data = response.json()

        for ticker in data:
            symbol = ticker['symbol']
            price = float(ticker['price'])
            if symbol in symbols:
                prices[symbol] = price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Binance.US prices: {e}")

    return prices

# Define the symbols you want to fetch prices for
symbols = ['BTCUSD', 'ETHUSD', 'AAVEUSD', 'UNIUSD', 'LINKUSD']

# Get the prices
prices = get_binance_us_prices(symbols)

# Print the prices
for symbol, price in prices.items():
    print(f"The current price of {symbol} is ${price:.2f}")
