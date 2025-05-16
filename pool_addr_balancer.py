import requests
from uni_token_analysis import tokens6
# Define GraphQL endpoint
url = 'https://api.thegraph.com/subgraphs/name/balancer-labs/balancer'

# Token addresses dictionary
tokens = {
    'BEL': '0xA91ac63D040dEB1b7A5E4d4134aD23eb0ba07e14',
    'AXS': '0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b',
    'ACH': '0xEd04915c23f00A313a544955524EB7DBD823143d',
    # Add remaining tokens here...
}

# Convert tokens dictionary to a list of (symbol, address) tuples
token_list = list(tokens6.items())


# Function to query The Graph API
def query_balancer(token1_address, token2_address):
    query = """
    {
      pools(where: {tokensList_contains: ["%s", "%s"]}) {
        id
        tokens {
          address
          balance
          weight
        }
      }
    }
    """ % (token1_address, token2_address)

    response = requests.post(url, json={'query': query})
    data = response.json()
    return data['data']['pools']


# Dictionary to store pool information
pool_info = {}

# Iterate over all token pairs
for i in range(len(token_list)):
    for j in range(i + 1, len(token_list)):
        token1_symbol, token1_address = token_list[i]
        token2_symbol, token2_address = token_list[j]

        pools = query_balancer(token1_address, token2_address)

        if pools:
            pool_info[f"{token1_symbol}-{token2_symbol}"] = pools

# Print the pool information
for pair, pools in pool_info.items():
    print(f"Pair: {pair}")
    for pool in pools:
        print(f"  Pool ID: {pool['id']}")
        for token in pool['tokens']:
            print(f"    Token Address: {token['address']}")
            print(f"    Balance: {token['balance']}")
            print(f"    Weight: {token['weight']}")
