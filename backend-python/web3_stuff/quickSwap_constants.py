# general imports
import json

QUICK_SWAP_FEE = 0.003

QUICK_ROUTER_ADDR = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"

router_abi_file = open("./web3_stuff/ABIs/quickSwap/quick_router_abi.json")
QUICK_ROUTER_ABI = json.load(router_abi_file)
