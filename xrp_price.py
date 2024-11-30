import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation

class XRPPriceTracker:
    def __init__(self, max_data_points=100):
        self.max_data_points = max_data_points
        self.timestamps = deque(maxlen=max_data_points)
        self.prices_usd = deque(maxlen=max_data_points)
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.line, = self.ax.plot([], [], 'b-', label='XRP/USD')
        self.setup_plot()
        
    def setup_plot(self):
        """Initialize the plot settings"""
        self.ax.set_title('XRP Price Live Chart (USD)', fontsize=14)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Price (USD)')
        self.ax.grid(True)
        self.ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

    def get_xrp_price(self):
        """Fetch XRP price data from CoinGecko API"""
        try:
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

    def display_price_info(self, price_data):
        """Display formatted price information"""
        if price_data:
            print('\nXRP Price Information:')
            print('-' * 50)
            print(f'USD Price: ${price_data["usd_price"]:.4f}')
            print(f'EUR Price: €{price_data["eur_price"]:.4f}')
            print(f'24h Change (USD): {price_data["usd_24h_change"]:.2f}%')
            print(f'Last Updated: {price_data["last_updated"].strftime("%Y-%m-%d %H:%M:%S")} UTC')
            print('-' * 50)

    def update_plot(self, frame):
        """Update function for the animation"""
        price_data = self.get_xrp_price()
        if price_data:
            self.display_price_info(price_data)
            
            # Add new data points
            self.timestamps.append(price_data['last_updated'])
            self.prices_usd.append(price_data['usd_price'])
            
            # Update plot data
            self.line.set_data(self.timestamps, self.prices_usd)
            
            # Update axes
            self.ax.set_xlim(min(self.timestamps), max(self.timestamps))
            if len(self.prices_usd) > 0:
                price_range = max(self.prices_usd) - min(self.prices_usd)
                self.ax.set_ylim(
                    min(self.prices_usd) - price_range * 0.1,
                    max(self.prices_usd) + price_range * 0.1
                )
            
            # Format x-axis
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            
            # Adjust layout
            plt.tight_layout()
        
        return self.line,

    def run(self):
        """Main function to run the price tracker with visualization"""
        print('XRP Price Tracker Started')
        print('Close the plot window to exit')
        
        # Create animation
        ani = FuncAnimation(
            self.fig, 
            self.update_plot, 
            interval=60000,  # Update every 60 seconds
            blit=True
        )
        
        plt.show()

def main():
    tracker = XRPPriceTracker()
    tracker.run()

if __name__ == '__main__':
    main()