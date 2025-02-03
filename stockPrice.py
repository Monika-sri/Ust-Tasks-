import time
import random

def stock_price_manipulator(base_price: float, volatility: float, steps: int):
    price = base_price 
    for _ in range(steps):
        change_percent = random.uniform(-volatility, volatility)
        price *= (1 + change_percent)
        print(f"Stock Price: {price:.2f}")
        time.sleep(1)  
stock_price_manipulator(base_price=200, volatility=0.03, steps=10)
