# general imports
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from eth_typing.evm import ChecksumAddress

# custom imports
from web3_stuff.global_constants import POLYGON_NETWORK_RPC
from web3_stuff.quickSwap_constants import QUICK_ROUTER_ADDR, QUICK_ROUTER_ABI
from web3_stuff.uniSwap_clone_funcs import get_exchange_price_single_token

PROVIDER: Web3 = Web3(HTTPProvider(POLYGON_NETWORK_RPC))

router_contract: Contract = PROVIDER.eth.contract(
    QUICK_ROUTER_ADDR, abi=QUICK_ROUTER_ABI
)


def run_quick(token_addr: ChecksumAddress):
    data = get_exchange_price_single_token(
        token_addr, router_contract, "QuickSwap.exchange"
    )
    return data
