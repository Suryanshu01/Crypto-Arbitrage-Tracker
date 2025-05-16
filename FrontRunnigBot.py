#imports the Web3 class from web3 module
from web3 import Web3  
# SEPOLIA_END_POINT ="https://eth-sepolia.g.alchemy.com/v2/c-4Mwxi1aTfQw8BEaHOiqGptxfRt1BDW"
main_net = "https://eth-mainnet.g.alchemy.com/v2/poqaFDjApt10JhJFW5MF0kdhfxIDauix"
w3 = Web3(Web3.HTTPProvider(main_net))
if w3.is_connected():
    
    tx_pool=w3.geth.txpool
    print(tx_pool.inspect())
    
else:
    
    print("You are not connected")
    


# if w3.is_connected():
    # {
    #     print(w3.eth.block_number,w3.eth.filter('pending'))
        
        

    # }

# print(w3.is_connected())        print(w3.eth.block_number)
