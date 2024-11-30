# XRP Price Tracker

A simple Python script that fetches real-time XRP (Ripple) price data using the CoinGecko API.

## Features

- Real-time XRP price tracking in USD and EUR
- 24-hour price change percentage
- Automatic updates every 60 seconds
- Clean console display
- No API key required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/imrealism/xrp_price.git
cd xrp_price
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:
```bash
python xrp_price.py
```

The script will continuously display:
- Current XRP price in USD and EUR
- 24-hour price change percentage
- Last update timestamp

To stop the script, press `Ctrl+C`.

## Sample Output
```
XRP Price Information:
--------------------------------------------------
USD Price: $0.6123
EUR Price: €0.5602
24h Change (USD): -2.45%
Last Updated: 2024-11-30 07:30:15 UTC
--------------------------------------------------
```

## Dependencies

- Python 3.6+
- requests
- python-dotenv

## Data Source

This script uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch XRP price data.

## License

MIT License