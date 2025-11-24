from binance.client import Client
import json

with open("config.json") as f:
    cfg = json.load(f)

api_key = cfg["api_key"]
api_secret = cfg["api_secret"]

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

order = client.create_order(
    symbol='BTCUSDT',
    side='BUY',
    type='MARKET',
    quantity=0.001
)

print("Order placed:")
print(order)
