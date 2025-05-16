import requests


def get_token_price(token_a, token_b, amount):
    url = f'https://api.0x.org/swap/v1/quote?sellToken={token_a}&buyToken={token_b}&sellAmount={amount}'
    headers = {
        'Content-Type': 'application/json',
        '0x-api-key': "e8b578c0-7bc4-4e73-b4ee-7f7aa7249eaa",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        price = data.get('price')
        return price
    else:
        print(f"Error fetching token price: {response.status_code}, {response.text}")
        return None


# Example usage

token_address = '0xTOKEN_ADDRESS'  # Replace with the token address you're interested in
token_price = get_token_price('0xA91ac63D040dEB1b7A5E4d4134aD23eb0ba07e14','0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b',1)
if token_price:
    print(f'Token price: {token_price}')
