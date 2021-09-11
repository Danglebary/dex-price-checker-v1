# General imports
from aiohttp import web
import socketio
import json
from time import sleep

# Custom imports
from web3_stuff.price_discovery_machine import run_exchanges

# Initialize web socket and http server, for development cors origins are
# set to wild-card, allowing any program to access this port.
# Do not recommend this for production.
sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

# Function called when web socket recieves a 'connect' event
@sio.event
def connect(sid, environ):
    print(f"[NEW CONNECTION] {sid}")


# Function called when web socket recieves a 'price_data_query' event,
# consuming a dict containing a list of exchanges, and a token name
# calls run_exchanges with given data,
# returning a priceData dict
@sio.event
async def price_data_query(sid, data):
    print(f"[SERVER] message recieved -> {data}")
    result = run_exchanges(data)
    print(f"[SERVER] message sent -> {result}")
    await sio.emit("price_data_response", {"data": result})


# Function called when web socket recieves a 'disconnect' event
@sio.event
def disconnect(sid):
    print(f"[CONNECTION CLOSED] client {sid} has disconnected")


# Function used to run the http server
def start_server():
    web.run_app(app, host="localhost", port=4000)
