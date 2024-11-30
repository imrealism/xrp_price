# XRP Price Tracker

A Python script that fetches real-time XRP (Ripple) price data using the CoinGecko API and displays it with a live updating chart.

## Features

- Real-time XRP price tracking in USD and EUR
- Live updating price chart visualization
- Historical price movement display (last 100 data points)
- 24-hour price change percentage
- Automatic updates every 60 seconds
- Clean console display
- No API key required

## Screenshots

The application provides both console output and a graphical visualization:

```
XRP Price Information:
--------------------------------------------------
USD Price: $0.6123
EUR Price: €0.5602
24h Change (USD): -2.45%
Last Updated: 2024-11-30 07:30:15 UTC
--------------------------------------------------
```

And a real-time updating chart showing price movements over time.

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

The script will:
- Display current XRP price in USD and EUR in the console
- Show 24-hour price change percentage
- Display the last update timestamp
- Open a window with a live-updating price chart
- Update both displays every 60 seconds

To stop the script:
- Close the chart window, or
- Press `Ctrl+C` in the console

## Dependencies

- Python 3.6+
- requests
- python-dotenv
- matplotlib
- numpy

## Data Source

This script uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch XRP price data.

## License

MIT License