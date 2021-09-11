from logging import addLevelName
from eth_typing.evm import ChecksumAddress
from web3 import Web3

# RPC
POLYGON_NETWORK_RPC: str = "https://polygon-rpc.com/"

# TOKENS AVAILABLE ON ALL CURRENTLY ADDED SWAPS
WETH_TOKEN_ADDR: ChecksumAddress = Web3.toChecksumAddress(
    "0x7ceb23fd6bc0add59e62ac25578270cff1b9f619"
)
MATIC_TOKEN_ADDR: ChecksumAddress = Web3.toChecksumAddress(
    "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
)
DAI_TOKEN_ADDR: ChecksumAddress = Web3.toChecksumAddress(
    "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
)
USDC_TOKEN_ADDR: ChecksumAddress = Web3.toChecksumAddress(
    "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
)
USDT_TOKEN_ADDR: ChecksumAddress = Web3.toChecksumAddress(
    "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
)

AVAILABLE_TOKENS = [
    {"token_name": "MATIC", "token_addr": MATIC_TOKEN_ADDR},
    {"token_name": "DAI", "token_addr": DAI_TOKEN_ADDR},
    {"token_name": "USDC", "token_addr": USDC_TOKEN_ADDR},
    {"token_name": "USDT", "token_addr": USDT_TOKEN_ADDR},
]
