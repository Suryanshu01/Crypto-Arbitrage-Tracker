# import requests
#
# def fetch_poloniex_prices():
#     url = 'https://poloniex.com/public?command=returnTicker'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check for HTTP errors
#
#         data = response.json()
#         for market, details in data.items():
#             print(f"{market}: Last price: {details['last']}")
#
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#     except Exception as err:
#         print(f"An error occurred: {err}")
#
# if __name__ == "__main__":
#     fetch_poloniex_prices()


# from poloniex import Poloniex
# polo = Poloniex()
# ticker = polo.returnTicker()['BTC_ETH']
# print(ticker)


import requests


def fetch_poloniex_prices():
    url = 'https://poloniex.com/public?command=returnTicker'
    try:
        response = requests.get(url)

        # Check for HTTP errors
        response.raise_for_status()

        # Attempt to parse the JSON response
        data = response.json()

        for market, details in data.items():
            print(f"{market}: Last price: {details['last']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    fetch_poloniex_prices()
