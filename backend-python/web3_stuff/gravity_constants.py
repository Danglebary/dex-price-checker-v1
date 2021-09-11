# general imports
import json

GRAVITY_SWAP_FEE = 0.003

GRAVITY_ROUTER_ADDR = "0x57dE98135e8287F163c59cA4fF45f1341b680248"

router_abi_file = open("./web3_stuff/ABIs/gravity/gravity_router_abi.json")
GRAVITY_ROUTER_ABI = json.load(router_abi_file)
