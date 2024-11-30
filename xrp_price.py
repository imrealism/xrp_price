import requests
import time
from datetime import datetime

def get_xrp_price():
    """Fetch XRP price data from CoinGecko API"""
    try:
        # CoinGecko API endpoint for XRP
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'ripple',
            'vs_currencies': 'usd,eur',
            'include_24hr_change': 'true',
            'include_last_updated_at': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract price data
        xrp_data = data['ripple']
        usd_price = xrp_data['usd']
        eur_price = xrp_data['eur']
        usd_24h_change = xrp_data['usd_24h_change']
        last_updated = datetime.fromtimestamp(xrp_data['last_updated_at'])
        
        return {
            'usd_price': usd_price,
            'eur_price': eur_price,
            'usd_24h_change': usd_24h_change,
            'last_updated': last_updated
        }
        
    except requests.exceptions.RequestException as e:
        print(f'Error fetching XRP price: {e}')
        return None

def display_price_info(price_data):
    """Display formatted price information"""
    if price_data:
        print('\nXRP Price Information:')
        print('-' * 50)
        print(f'USD Price: ${price_data["usd_price"]:.4f}')
        print(f'EUR Price: €{price_data["eur_price"]:.4f}')
        print(f'24h Change (USD): {price_data["usd_24h_change"]:.2f}%')
        print(f'Last Updated: {price_data["last_updated"].strftime("%Y-%m-%d %H:%M:%S")} UTC')
        print('-' * 50)

def main():
    """Main function to run the price fetcher"""
    print('XRP Price Fetcher Started')
    print('Press Ctrl+C to exit')
    
    try:
        while True:
            price_data = get_xrp_price()
            display_price_info(price_data)
            # Wait for 60 seconds before next update
            time.sleep(60)
            
    except KeyboardInterrupt:
        print('\nProgram terminated by user')

if __name__ == '__main__':
    main()