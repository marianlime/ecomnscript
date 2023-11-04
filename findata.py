import random
import csv
from datetime import datetime,time, timedelta

symbols = ['AAPL', 'TSLA', 'NVDA','PLTR', 'MSFT', 'VFS', 'AMZN','FTNT','O','KO']
start_date = datetime(2018, 1, 1)
end_date = datetime(2022, 12, 31)
start_time = time(9, 0)
end_time = time(17, 0)
delta = timedelta(seconds=45)

with open('not_real_tick_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Symbol', 'Price', 'Timestamp'])
    
    current_date = start_date
    while current_date <= end_date:
        current_time = current_date.time()
        
        if start_date <= current_date <= end_date:
            symbol = random.choice(symbols)
            price = round(random.uniform(250, 800), 2)
            timestamp = current_date.strftime(' %Y-%m-%d %H:%M:%S')
            csvwriter.writerow([symbol, price, timestamp])
        
        
        current_date += delta
        
        if current_time >= end_time:
            next_day = current_date + timedelta(days=1)
            current_date = datetime(next_day.year, next_day.month, next_day.day, start_time.hour, start_time.minute)
            
        
        if current_date > end_date:
            break