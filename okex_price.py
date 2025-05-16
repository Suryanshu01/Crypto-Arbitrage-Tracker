import requests


def fetch_okex_prices():
    url = 'https://www.okx.com/api/v5/market/tickers?instType=SPOT'
    try:
        response = requests.get(url)

        # Check for HTTP errors
        response.raise_for_status()

        # Attempt to parse the JSON response
        data = response.json()

        # Check if the response contains the ticker data
        if 'data' in data:
            for ticker in data['data']:
                instrument = ticker['instId']
                last_price = ticker['last']
                print(f"{instrument}: Last price: {last_price}")
        else:
            print("No ticker data found in the response")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    fetch_okex_prices()
