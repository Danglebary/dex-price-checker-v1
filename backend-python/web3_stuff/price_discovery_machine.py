# Custom imports
from web3_stuff.apeSwap import run_ape
from web3_stuff.gravity import run_gravity
from web3_stuff.polycat import run_polycat
from web3_stuff.quickSwap import run_quick
from web3_stuff.sushiSwap import run_sushi

from web3_stuff.global_constants import AVAILABLE_TOKENS

ALL_EXCHANGES = {
    "APESWAP": run_ape,
    "GRAVITY": run_gravity,
    "POLYCAT": run_polycat,
    "QUICKSWAP": run_quick,
    "SUSHISWAP": run_sushi,
}

# Function consuming a dicts of exchange names and a token name
#   calling the run function for each exchange given
#   returning a list of priceData dicts
def run_exchanges(data: dict[list[str], str]):
    exchanges: list = data["exchanges"]
    token: str = data["token"]

    token_addr = next(
        item for item in AVAILABLE_TOKENS if item["token_name"] == token
    )

    exchange_prices = []
    for exchange in exchanges:
        func = ALL_EXCHANGES.get(exchange)
        exchange_data = func(token_addr["token_addr"])

        exchange_prices.append(exchange_data)

    return exchange_prices
