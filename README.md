
# Binance Spot Testnet Trading Bot

## Overview
This project demonstrates a simplified trading bot in Python that connects to the Binance Spot Testnet.  
It uses the official `python-binance` library to place a market buy order and prints the order details to the console.

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `config.json` file with your Spot Testnet API keys:
   ```json
   {
     "api_key": "YOUR_API_KEY",
     "api_secret": "YOUR_API_SECRET"
   }
   ```

## Usage
Run the bot with:
```bash
python bot.py
```

The script will:
- Connect to Binance Spot Testnet (`https://testnet.binance.vision`)
- Place a market buy order for `BTCUSDT`
- Print the order details (orderId, status, fills, etc.)

## Example Output
```
Order placed:
{'symbol': 'BTCUSDT', 'orderId': 3657318, 'status': 'FILLED', 'type': 'MARKET', 'side': 'BUY', ...}
```

## Notes
- This bot is for **educational and testing purposes only**.  
- It uses the Binance Spot Testnet, so no real funds are involved.  
- Extendable to support limit or stop-limit orders if required.
```

