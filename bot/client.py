from binance.client import Client

API_KEY = "test"
API_SECRET = "test"

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com"
    return client