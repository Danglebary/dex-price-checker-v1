# general imports
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from eth_typing.evm import ChecksumAddress

# custom imports
from web3_stuff.global_constants import POLYGON_NETWORK_RPC
from web3_stuff.sushiSwap_constants import (
    SUSHISWAP_ROUTER_ADDR,
    SUSHISWAP_ROUTER_ABI,
)
from web3_stuff.uniSwap_clone_funcs import get_exchange_price_single_token

PROVIDER: Web3 = Web3(HTTPProvider(POLYGON_NETWORK_RPC))

router_contract: Contract = PROVIDER.eth.contract(
    SUSHISWAP_ROUTER_ADDR, abi=SUSHISWAP_ROUTER_ABI
)


def run_sushi(token_addr: ChecksumAddress):
    data = get_exchange_price_single_token(
        token_addr, router_contract, "SushiSwap"
    )
    return data
