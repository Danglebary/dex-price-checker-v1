# general imports
import json

POLY_SWAP_FEE = 0.0024

POLYCAT_ROUTER_ADDR: str = "0x94930a328162957FF1dd48900aF67B5439336cBD"

router_abi_file = open("./web3_stuff/ABIs/polycat/polycat_router_abi.json")
POLYCAT_ROUTER_ABI: dict = json.load(router_abi_file)
