# General imports
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from eth_typing.evm import ChecksumAddress

# Custom imports
from web3_stuff.global_constants import POLYGON_NETWORK_RPC, WETH_TOKEN_ADDR
from web3_stuff.format_nums import format_num

PROVIDER = Web3(HTTPProvider(POLYGON_NETWORK_RPC))

# Function consuming an exchanges router contract and a token address,
#   returning the current price of the given token derived in Ether
def get_single_token_derived_eth(
    token_addr: ChecksumAddress, router_contract: Contract
):
    res = router_contract.functions.getAmountsOut(
        1000000000000000000, [token_addr, WETH_TOKEN_ADDR]
    ).call()

    price = format_num(res[1])
    return price


# Function consuming an exchanges router contract, exchange name, and a token address,
#   returning a priceData object containing the name of the exchange and the current price
#   derived in Ether
def get_exchange_price_single_token(
    token_addr: ChecksumAddress, router_contract: Contract, exchange_name: str
):
    price = get_single_token_derived_eth(token_addr, router_contract)
    price = str(price)
    data = {"exchange_name": exchange_name, "current_price": price}
    return data
