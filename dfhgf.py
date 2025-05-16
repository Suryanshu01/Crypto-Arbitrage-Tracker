import json
from web3 import Web3, HTTPProvider
import requests

RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/UcLnaPDIR4S2rplgaMDMe_g0VmTt4sJ1"

W3 = Web3(HTTPProvider(RPC_URL))

VARIABLE_COIN = [
    'bel',
    'axs',
    'ach',
    'cake',
    '8pay',
    'aave',
    'ach',
    'ada',
    'adx',
    'alice',
    'alpa',
    'alpaca',
    'alpha',
    'ampl',
    'ankr',
    'ankrbnb',
    'antex',
    'anymtlx',
    'aog',
    'ape',
    'apx',
    'apys',
    'arena',
    'arpa',
    'arv',
    'asr',
    'ata',
    'atm',
    'atom',
    'axl',
    'axs',
    'babycake',
    'bake',
    'balbt',
    'band',
    'bat',
    'bath',
    'bbt',
    'bcfx',
    'c98',
    "eth",
    "btcb",
    "usdc",
    "fxs",
    "mc",
    "frax",
    "dai",
    "woo",
    "uni",
    "super",
]
SOLID_COIN = ["weth", "usdt", "usdc", "btcb", "eth"]
COINS = {
    "usdt": "0x55d398326f99059fF775485246999027B3197955",
    "weth": "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA",
    "eth": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
    "btcb": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
    "usdc": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
    "fxs": "0xe48A3d7d0Bc88d552f730B62c006bC925eadB9eE",
    "mc": "0x949D48EcA67b17269629c7194F4b727d4Ef9E5d6",
    "frax": "0x90C97F71E18723b0Cf0dfa30ee176Ab653E89F40",
    "dai": "0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3",
    "woo": "0x4691937a7508860F876c9c0a2a617E7d9E945D4B",
    "uni": "0xBf5140A22578168FD562DCcF235E5D43A02ce9B1",
    "super": "0x51BA0b044d96C3aBfcA52B64D733603CCC4F0d4D",
    "wbnb": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    "cell": "0xd98438889Ae7364c7E2A3540547Fad042FB24642",
    "sand": "0x67b725d7e342d7B611fa85e859Df9697D9378B2e",
    "shib": "0x2859e4544C4bB03966803b044A93563Bd2D0DD4D",
    'bel': '0x8443f091997f06a61670B735ED92734F5628692F',
    'axs': '0x715D400F88C167884bbCc41C5FeA407ed4D2f8A0',
    'ach': '0xBc7d6B50616989655AfD682fb42743507003056D',
    "cake": "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82",
    "8pay": "0xFeea0bDd3D07eb6FE305938878C0caDBFa169042",
    "aave": "0xfb6115445Bff7b52FeB98650C87f44907E58f802",
    "ach": "0xBc7d6B50616989655AfD682fb42743507003056D",
    "ada": "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47",
    "adx": "0x6bfF4Fb161347ad7de4A625AE5aa3A1CA7077819",
    "alice": "0xAC51066d7bEC65Dc4589368da368b212745d63E8",
    "alpa": "0xc5E6689C9c8B02be7C49912Ef19e79cF24977f03",
    "alpaca": "0x8F0528cE5eF7B51152A59745bEfDD91D97091d2F",
    "alpha": "0xa1faa113cbE53436Df28FF0aEe54275c13B40975",
    "ampl": "0xDB021b1B247fe2F1fa57e0A87C748Cc1E321F07F",
    "ankr": "0xf307910A4c7bbc79691fD374889b36d8531B08e3",
    "ankrbnb": "0x52F24a5e03aee338Da5fd9Df68D2b6FAe1178827",
    "antex": "0xCA1aCAB14e85F30996aC83c64fF93Ded7586977C",
    "anymtlx": "0x5921DEE8556c4593EeFCFad3CA5e2f618606483b",
    "aog": "0x40C8225329Bd3e28A043B029E0D07a5344d2C27C",
    "ape": "0xC762043E211571eB34f1ef377e5e8e76914962f9",
    "apx": "0x78F5d389F5CDCcFc41594aBaB4B0Ed02F31398b3",
    "apys": "0x37dfACfaeDA801437Ff648A1559d73f4C40aAcb7",
    "arena": "0xCfFD4D3B517b77BE32C76DA768634dE6C738889B",
    "arpa": "0x6F769E65c14Ebd1f68817F5f1DcDb61Cfa2D6f7e",
    "arv": "0x6679eB24F59dFe111864AEc72B443d1Da666B360",
    "asr": "0x80D5f92C2c8C682070C95495313dDB680B267320",
    "ata": "0xA2120b9e674d3fC3875f415A7DF52e382F141225",
    "atm": "0x25E9d05365c867E59C1904E7463Af9F312296f9E",
    "atom": "0x0Eb3a705fc54725037CC9e008bDede697f62F335",
    "axl": "0x8b1f4432F943c465A973FeDC6d7aa50Fc96f1f65",
    "axs": "0x715D400F88C167884bbCc41C5FeA407ed4D2f8A0",
    "babycake": "0xdB8D30b74bf098aF214e862C90E647bbB1fcC58c",
    "bake": "0xE02dF9e3e622DeBdD69fb838bB799E3F168902c5",
    "balbt": "0x72fAa679E1008Ad8382959FF48E392042A8b06f7",
    "band": "0xAD6cAEb32CD2c308980a548bD0Bc5AA4306c6c18",
    "bat": "0x101d82428437127bF1608F699CD651e6Abf9766E",
    "bath": "0x0bc89aa98Ad94E6798Ec822d0814d934cCD0c0cE",
    "bbt": "0xD48474E7444727bF500a32D5AbE01943f3A59A64",
    "bcfx": "0x045c4324039dA91c52C55DF5D785385Aab073DcF",
    "c98": "0xaEC945e04baF28b135Fa7c640f624f8D90F1C3a6"
}

# Uniswap configuration
uniswap_router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
uniswap_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
uniswap_abi_url = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + uniswap_router_address
response = requests.get(uniswap_abi_url)
uniswap_abi = response.json()["result"]
with open('factory.json') as f:
    factory_abi = (json.load(f))['result']

fact_contr=W3.eth.contract(address=uniswap_factory_address, abi=factory_abi)
#
# for sCoin in SOLID_COIN:
#     for vCoin in VARIABLE_COIN:
#         pair_address = fact_contr.functions.getPair(COINS[vCoin], COINS[sCoin]).call()
#         if not pair_address == "0x0000000000000000000000000000000000000000":
#             print("yes")
#         else:
#             print(".")

print(W3.to_checksum_address("0xbb0e17ef65f82ab018d8edd776e8dd940327b28b"))