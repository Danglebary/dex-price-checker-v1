# general imports
import json

from eth_typing.evm import Address

SUSHI_SWAP_FEE = 0.003

SUSHISWAP_ROUTER_ADDR: str = "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"

router_abi_file = open("./web3_stuff/ABIs/sushiSwap/sushi_router_abi.json")
SUSHISWAP_ROUTER_ABI: dict = json.load(router_abi_file)
