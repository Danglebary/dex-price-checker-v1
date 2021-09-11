# general imports
import json

APE_SWAP_FEE = 0.002

APESWAP_ROUTER_ADDR = "0xC0788A3aD43d79aa53B09c2EaCc313A787d1d607"

router_abi_file = open("./web3_stuff/ABIs/apeSwap/ape_router_abi.json")
APESWAP_ROUTER_ABI: dict = json.load(router_abi_file)
