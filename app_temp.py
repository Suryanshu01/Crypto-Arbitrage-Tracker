from uniswap import Uniswap
def get_uniswap_price_v2(contract, token_a, token_b, amount):
    try:
        address = None  # or None if you're not going to make transactions
        private_key = None  # or None if you're not going to make transactions
        version = 2  # specify which version of Uniswap to use
        provider = "https://eth-mainnet.g.alchemy.com/v2/UcLnaPDIR4S2rplgaMDMe_g0VmTt4sJ1"
        uniswap = Uniswap( address=address, private_key=private_key, version=version, provider=provider)
        decimal_a = 18
        decimal_b = 18
        prices = uniswap.get_price_input(token_a, token_b, amount * 10 ** decimal_a)
        return (prices / (10 ** decimal_b))
    except Exception as e:
        #       print(prices)
        print(f"and Expectedd error has occurred {e}")
        return (0, 'NULL')
    # print(prices)



print(get_uniswap_price_v2(contract=None, token_a="0x0D8775F648430679A709E98d2b0Cb6250d2887EF", token_b="0x6B175474E89094C44Da98b954EedeAC495271d0F", amount=10000 ))