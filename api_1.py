import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import sqlite3
import sqlalchemy
conn = sqlite3.connect('a1.db')
style.use('fivethirtyeight')
#api_key=open('alpha.txt','r').read()
#sapi_key='xxx'
API_URL = "https://www.alphavantage.co/query"
#TAKING DATA FROM API AS JSON 
#symbols = ['QCOM']
data = { "function": "TIME_SERIES_INTRADAY", 
        "symbol": "QCOM",
        "interval" : "60min",
	"outputsize":"full",       
        "datatype": "json", 
        "apikey": "XXX" } 
response = requests.get(API_URL, data)
data=response.json()
data=data['Time Series (60min)']
#USING PANDA TO CREATE DATA FRAMES
df=pd.DataFrame(columns=['date','open','high','low','close','volume'])
for d,p in data.items():
    date=datetime.datetime.strptime(d,'%Y-%m-%d %H:%M:%S')
    data_row=[date,float(p['1. open']),float(p['2. high']),float(p['3. low']),float(p['4. close']),int(p['5. volume'])]
    df.loc[-1,:]=data_row
    df.index=df.index+1
data=df.sort_values('date')

data['close']=data['close'].astype(float)
data['5min']=np.round(data['close'].rolling(window=5).mean(),2)
print(data['close'])
data[['5min','close']].plot()
plt.show()
#PASSING DATA FRAMES TO DATABASE
data.to_sql('tab', conn, if_exists='replace', index=True)
pd.read_sql('select * from tab', conn)


