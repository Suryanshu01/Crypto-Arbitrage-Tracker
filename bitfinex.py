import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Suppress the InsecureRequestWarning when SSL verification is disabled
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class BITFINEX:
    def get_bitfinex_price(symbol):
        url = f"https://api-pub.bitfinex.com/v2/ticker/{symbol}"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()
            price = data[6]  # Assuming the price index is consistent across all tickers
            return price
        else:
            return None


    # Define the symbols you want to fetch prices for
    # Note: Bitfinex uses different symbol formats, e.g., tBTCUSD for BTC/USD
    symbols = ['tBTCUSD', 'tETHUSD', 'tAAVEUSD', 'tUNIUSD', 'tLINKUSD']

# Get the prices
# prices = get_bitfinex_prices(symbols)
#
# # Print the prices
# for symbol, price in prices.items():
#     if price:
#         print(f"The current price of {symbol} is ${price}")
#     else:
#         print(f"Failed to fetch the price for {symbol}")


# print(BITFINEX.get_bitfinex_price('tAXSUSD'))


# import requests
#
#
# def fetch_token_price(token_symbol):
#     # Construct the URL for the Bitfinex API
#     url = f'https://api.bitfinex.com/v1/pubticker/{token_symbol}usd'
#
#     try:
#         # Make a GET request to the API
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an error for bad responses
#
#         # Parse the JSON response
#         data = response.json()
#
#         # Check if the response contains the price
#         if 'last_price' in data:
#             return float(data['last_price'])
#         else:
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return None
#
#
# if __name__ == "__main__":
#     token = input("Enter the token symbol (e.g., BTC, ETH): ").upper()
#     price = fetch_token_price(token)
#
#     if price is not None:
#         print(f"The current price of {token} is: ${price}")
#     else:
#         print(f"Could not fetch the price for {token}. Please check the token symbol.")
