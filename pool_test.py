import requests
import pandas as pd
from datetime import datetime, timedelta

# Define the Uniswap Subgraph API endpoint
UNISWAP_API_URL = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"

# GraphQL query to fetch pool data
query = """
{
  pools(first: 1000, orderBy: totalLiquidity, orderDirection: desc) {
    id
    token0 {
      symbol
    }
    token1 {
      symbol
    }
    reserveUSD
    volumeUSD
    createdAtTimestamp
  }
}
"""


def fetch_pools():
    response = requests.post(UNISWAP_API_URL, json={'query': query})
    if response.status_code == 200:
        return response.json()['data']['pools']
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


def calculate_stability(pools):
    # For simplicity, let's consider stability as pools with the highest liquidity
    # Further refinement can be done based on other criteria
    pools_df = pd.DataFrame(pools)
    pools_df['reserveUSD'] = pools_df['reserveUSD'].astype(float)
    pools_df['createdAtTimestamp'] = pd.to_datetime(pools_df['createdAtTimestamp'], unit='s')

    # Filter pools created more than 30 days ago
    one_month_ago = datetime.now() - timedelta(days=30)
    stable_pools = pools_df[pools_df['createdAtTimestamp'] < one_month_ago]

    # Sort by liquidity
    stable_pools = stable_pools.sort_values(by='reserveUSD', ascending=False)

    return stable_pools


if __name__ == "__main__":
    pools = fetch_pools()
    stable_pools = calculate_stability(pools)

    # Display the top 10 stable pools
    print("Top 10 Stable Pools on Uniswap:")
    print(stable_pools[['token0', 'token1', 'reserveUSD', 'createdAtTimestamp']].head(10))
