import requests

class HUOBI():
    def get_huobi_price(symbol):
        url = f"https://api.huobi.pro/market/detail/merged?symbol={symbol}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                ticker = data['tick']
                price = ticker['close']
                return price
            else:
                return None
        else:
            return None


    # Define the symbols you want to fetch prices for
    # Note: Huobi uses different symbol formats, e.g., btcusdt for BTC/USDT
    symbols = ['btcusdt', 'ethusdt', 'aaveusdt', 'unieth', 'linkusdt']

    # Get the prices
    # prices = get_huobi_prices(symbols)

# Print the prices
# for symbol, price in HUOBI.prices.items():
#     if price:
#         print(f"The current price of {symbol.upper()} is ${price}")
#     else:
#         print(f"Failed to fetch the price for {symbol.upper()}")

# print(HUOBI.get_huobi_price('btcusdt'))