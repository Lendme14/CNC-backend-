from web3 import Web3

bsc_test_rpc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
contract_address = "0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8"
ABI = []  # Replace with actual ABI

w3 = Web3(Web3.HTTPProvider(bsc_test_rpc))
contract = w3.eth.contract(address=contract_address, abi=ABI)

def get_token_balance(user_address):
    return contract.functions.balanceOf(user_address).call() / 1e18