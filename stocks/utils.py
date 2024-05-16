    
from datetime import datetime

from stocks.models import Stock


def get_stocks():
    symbols = [
    "AAPL",  
    "MSFT",  
    "AMZN",  
    "GOOGL", 
    "FB",    
    "TSLA",  
    "JPM",   
    "V",     
    "NVDA",  
    "DIS",   
    "NFLX",  
    "GS",    
    "WMT",   
    "PG",    
    "KO",    
    "IBM",   
    "PEP",   
    "INTC",  
    "CSCO",  
    "ORCL",  
    "HD",    
    "MCD",   
    "BA",    
    "CAT",   
    "MMM",   
    "XOM",   
    "CVX",   
    "WBA",   
    "UNH",   
    "GS",    
    "AXP",   
    "NKE",   
    "MS",    
    "PYPL",  
    "COST",  
    "CMCSA", 
    "T",     
    "AMD",   
    "NIO",   
    "UBER",  
    "ZM",    
    "SNAP",  
    "SQ",    
    "TWTR",  
    "ROKU",  
    "SHOP",  
    "AMAT",  
    "EA",    
    "ROK",   
    "CRM",   
    "ADBE",  
    "NVAX",  
    "GILD",  
    "MRNA",  
    "ZS",    
    "PINS",  
    "DOCU",  
    "NOW",   
    "UBER",  
    "SQ",    
    "ROKU",  
    "SHOP",  
    "AMAT",  
    "EA",    
    "ROK",   
    "CRM",   
    "ADBE",  
    "NVAX",  
    "GILD",  
    "MRNA",  
    "ZS",    
    "PINS",  
    "DOCU",  
    "NOW",   
    "GME",   
    "BB",    
    "F",     
    "GE",    
    "C",     
    "BABA",  
    "JD",    
    "BAC",   
    "AAP",   
    "AAL",   
    "DAL",   
    "UAL",   
    "NFLX",  
    "AMC",   
    "GPRO",  
    "UBER",  
    "LYFT",  
    "SPCE",  
    "NOK",   
    "BBBY",  
    "BBY",   
    "CCL",   
    "RCL",   
    "NCLH",  
    "TGT",   
    "M",     
    "TJX",   
    "SHLDQ", 
    "JCPNQ", 
    "GPS",   
    "TIF",   
    "HBI",   
    "JWN",   
    ]
    stocks = [
{'symbol': 'MSFT', 'timestamp': '2024-04-14 23:32:12', 'low': 221.67, 'high': 560.06, 'close': 415.87, 'timezone': 'US/Mountain', 'volume': 214},{'symbol': 'AMZN', 'timestamp': '2024-04-30 21:08:41', 'low': 408.19, 'high': 550.88, 'close': 485.86, 'timezone': 'US/Eastern', 'volume': 344},{'symbol': 'GOOGL', 'timestamp': '2024-01-13 03:28:37', 'low': 441.83, 'high': 567.91, 'close': 445.09, 'timezone': 'US/Mountain', 'volume': 107},{'symbol': 'FB', 'timestamp': '2024-05-07 05:57:59', 'low': 191.84, 'high': 446.36, 'close': 193.01, 'timezone': 'US/Central', 'volume': 
366},
{'symbol': 'TSLA', 'timestamp': '2024-02-06 05:54:48', 'low': 340.49, 'high': 443.88, 'close': 410.97, 'timezone': 'US/Pacific', 'volume': 304},{'symbol': 'JPM', 'timestamp': '2024-04-15 19:52:14', 'low': 489.43, 'high': 524.19, 'close': 516.07, 'timezone': 'US/Eastern', 'volume': 467},{'symbol': 'V', 'timestamp': '2024-03-30 00:09:45', 'low': 469.05, 'high': 482.93, 'close': 469.52, 'timezone': 'US/Eastern', 'volume': 121},{'symbol': 'NVDA', 'timestamp': '2024-03-01 00:46:58', 'low': 490.27, 'high': 524.71, 'close': 494.23, 'timezone': 'US/Eastern', 'volume': 
135},
{'symbol': 'DIS', 'timestamp': '2024-01-02 21:04:20', 'low': 231.18, 'high': 587.32, 'close': 470.62, 'timezone': 'US/Mountain', 'volume': 377},{'symbol': 'NFLX', 'timestamp': '2024-02-23 06:24:19', 'low': 112.23, 'high': 160.87, 'close': 131.03, 'timezone': 'US/Eastern', 'volume': 433},{'symbol': 'GS', 'timestamp': '2024-04-24 20:21:58', 'low': 201.16, 'high': 414.66, 'close': 339.8, 'timezone': 'US/Mountain', 'volume': 195},{'symbol': 'WMT', 'timestamp': '2024-02-21 11:41:27', 'low': 358.89, 'high': 457.01, 'close': 365.47, 'timezone': 'US/Mountain', 'volume': 203},{'symbol': 'PG', 'timestamp': '2024-03-18 01:37:06', 'low': 286.29, 'high': 553.37, 'close': 354.48, 'timezone': 'US/Pacific', 'volume': 332},{'symbol': 'KO', 'timestamp': '2024-02-02 15:38:43', 'low': 471.99, 'high': 472.37, 'close': 472.04, 'timezone': 'US/Pacific', 'volume': 
334},
{'symbol': 'IBM', 'timestamp': '2024-03-14 16:29:13', 'low': 406.63, 'high': 470.21, 'close': 459.21, 'timezone': 'US/Mountain', 'volume': 316},{'symbol': 'PEP', 'timestamp': '2024-03-17 07:17:19', 'low': 447.92, 'high': 466.21, 'close': 463.0, 'timezone': 'US/Central', 'volume': 
420},
{'symbol': 'INTC', 'timestamp': '2024-03-09 12:37:08', 'low': 163.05, 'high': 379.47, 'close': 337.71, 'timezone': 'US/Eastern', 'volume': 353},{'symbol': 'CSCO', 'timestamp': '2024-02-28 01:44:55', 'low': 498.32, 'high': 581.25, 'close': 553.94, 'timezone': 'US/Mountain', 'volume': 397},{'symbol': 'ORCL', 'timestamp': '2024-04-04 12:44:21', 'low': 197.99, 'high': 223.31, 'close': 220.8, 'timezone': 'US/Pacific', 'volume': 332},{'symbol': 'HD', 'timestamp': '2024-02-17 16:08:52', 'low': 366.42, 'high': 514.0, 'close': 474.95, 'timezone': 'US/Eastern', 'volume': 211},{'symbol': 'MCD', 'timestamp': '2024-05-14 11:44:46', 'low': 104.2, 'high': 536.0, 'close': 200.73, 'timezone': 'US/Central', 'volume': 140},{'symbol': 'BA', 'timestamp': '2024-01-02 10:43:40', 'low': 497.14, 'high': 588.37, 'close': 527.29, 'timezone': 'US/Central', 'volume': 130},{'symbol': 'CAT', 'timestamp': '2024-03-20 17:30:15', 'low': 333.13, 'high': 422.7, 'close': 385.04, 'timezone': 'US/Mountain', 'volume': 277},{'symbol': 'MMM', 'timestamp': '2024-02-02 08:48:05', 'low': 448.41, 'high': 503.41, 'close': 452.81, 'timezone': 'US/Pacific', 'volume': 270},

    ]
    return stocks
    import requests
    for symbol in symbols[:25]:
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=87CDISIEWYYG2B88'
        r = requests.get(url)
        data = r.json()
        
        

        meta_data = data.get('Meta Data', {})
        time_series_data = data.get('Time Series (5min)', {})
        timezone = meta_data.get('6. Time Zone')

        latest_timestamp_str = meta_data.get('3. Last Refreshed')

        latest_data = time_series_data.get(latest_timestamp_str, {})
        low = latest_data.get('3. low')
        high = latest_data.get('2. high')
        close = latest_data.get('4. close')
        volume = latest_data.get("5. volume")
        serialized_data = {
        'symbol': symbol,
        'timestamp': latest_timestamp_str,
        'low': low,
        'high': high,
        'close': close,
        'timezone': timezone,
        'volume':volume
        }   
        print(serialized_data)
        stocks.append(serialized_data)
    return stocks


def populate_stocks(stocks):
    Stock.objects.bulk_create([Stock(**data) for data in stocks])