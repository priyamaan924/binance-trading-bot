# Binance Futures Testnet Trading Bot

## Features
- Market & Limit Orders
- BUY / SELL support
- CLI-based input
- Logging system
- Error handling

## Setup
1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Add .env file with API keys

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Assumptions
- User has Binance Futures Testnet account
- API keys are valid

## Logs
Stored in logs/trading.log