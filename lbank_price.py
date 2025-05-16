import requests


class LBANK():

    def fetch_lbank_price(symbol):
        # LBank API endpoint for getting ticker price
        url = f"https://api.lbkex.com/v2/ticker.do?symbol={symbol}"

        try:
            response = requests.get(url)
            data = response.json()

            if data['result'] == 'true':
                ticker_info = data['data'][0]
                price = ticker_info['ticker']['latest']
                return price
            else:
                # print(f"Error fetching price data: {data['error_code']}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


LBANK.fetch_lbank_price("UNI")