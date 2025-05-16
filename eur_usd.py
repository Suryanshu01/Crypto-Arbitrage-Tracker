import requests


def get_eur_to_usd():
    # You can get a free API key from https://www.exchangerate-api.com/
    api_key = "acd9ac9ffd9dbe7f38594f0d"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/EUR/USD"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            eur_to_usd_rate = data['conversion_rate']
            # print(f"Current EUR to USD exchange rate: {eur_to_usd_rate}")
            return eur_to_usd_rate
        else:
            print(f"Error: {data['error-type']}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Fetch and print the exchange rate
get_eur_to_usd()
