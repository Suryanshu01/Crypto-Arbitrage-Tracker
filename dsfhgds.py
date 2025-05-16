from uniswap import Uniswap

address = None          # or None if you're not going to make transactions
private_key = None  # or None if you're not going to make transactions
version = 2                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/295ac0e95bb4437c8e638317bb00ebc4"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"

x=uniswap.get_price_input(eth, dai, 10**18)
dai_eth_price = uniswap.get_price_input(eth, dai, 10**18)

# Get the price of BAT in terms of ETH
bat_eth_price = uniswap.get_price_input(eth, bat, 10**18)

# Calculate the price of DAI in terms of BAT
dai_bat_price = dai_eth_price / bat_eth_price

print(f"1 DAI = {dai_bat_price:.6f} BAT")
print(x/10**18)


from dfhgf import Decimal

# Get the number of decimal places for each coin (replace with actual values)
eth_decimals = 18  # Example: Ethereum has 18 decimal places
dai_decimals = 18  # Example: DAI has 18 decimal places
bat_decimals = 18  # Example: BAT has 18 decimal places

# Get the price of DAI in terms of ETH
dai_eth_price = uniswap.get_price_input(eth, dai, 10**eth_decimals)

# Get the price of BAT in terms of ETH
bat_eth_price = uniswap.get_price_input(eth, bat, 10**eth_decimals)

# Calculate the price of DAI in terms of BAT
dai_bat_price = dai_eth_price / bat_eth_price

# Convert the result to Decimal for proper decimal handling
dai_bat_price_decimal = Decimal(dai_bat_price) / Decimal(10**bat_decimals)

print(f"1 DAI = {dai_bat_price_decimal:.6f} BAT")