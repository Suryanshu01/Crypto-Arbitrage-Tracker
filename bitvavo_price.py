import requests
from python_bitvavo_api.bitvavo import Bitvavo
class BITVAVO():
    def get_bitvavo_prices(symbol):
        bitvavo = Bitvavo()


        # prices = {}


        response = bitvavo.tickerPrice({'market': symbol})
        if 'errorCode' not in response:

              prices = response['price']
        else:
              prices = None

        return prices


    # Define the symbols you want to fetch prices for
    # Note: Bitvavo uses different symbol formats, e.g., BTC-EUR for BTC/EUR
    symbols = ['BTC-EUR', 'ETH-EUR', 'AAVE-EUR', 'UNI-EUR', 'LINK-EUR']

    # Get the prices
    # prices = get_bitvavo_prices(symbols)

# Print the prices
# for symbol, price in BITVAVO.prices.items():
#     if price:
#         print(f"The current price of {symbol} is €{price}")
#     else:
#         print(f"Failed to fetch the price for {symbol}")

# print(BITVAVO.get_bitvavo_prices("BTC-EUR"))








