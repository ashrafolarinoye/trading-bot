import ccxt
import talib

# Connect to your exchange API
exchange = ccxt.exchange_name({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY'
})

# Define the symbol you want to trade
symbol = 'BTC/USD'

# Define the RSI period
rsi_period = 14

# Define the initial amount of US dollars you want to use for trading
usd_amount = 1000

# Loop through daily candles
while True:
    # Get the last 100 daily candles
    ohlcv = exchange.fetch_ohlcv(symbol, '1d', limit=100)
    
    # Extract closing prices from OHLCV data
    close_prices = [candle[4] for candle in ohlcv]
    
    # Calculate RSI for the last 14 periods
    rsi = talib.RSI(close_prices, rsi_period)
    
    # Get the last RSI value
    current_rsi = rsi[-1]
    
    # Check if RSI is below 30
    if current_rsi < 30:
        # Buy Bitcoin with your US dollars
        order = exchange.create_market_buy_order(symbol, usd_amount)
        print(f"Bought {order['amount']} {symbol} at {order['price']} USD")
    
    # Check if RSI is above 70
    elif current_rsi > 70:
        # Sell your Bitcoin for US dollars
        amount = exchange.fetch_balance()[symbol]['free']
        order = exchange.create_market_sell_order(symbol, amount)
        print(f"Sold {order['amount']} {symbol} at {order['price']} USD")
    
    # Wait for 24 hours before checking again
    time.sleep(24 * 60 * 60)