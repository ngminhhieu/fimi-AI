import requests
import pandas as pd
from datetime import datetime

data = pd.read_csv('./app/data/fimi02.csv', usecols=['DATE', 'TIME', 'PM2.5'])
data['datetime'] = data['DATE'] + " " + data['TIME']
data['datetime'] = pd.to_datetime(data['datetime'], format='%Y/%m/%d %H:%M:%S')
df = pd.DataFrame(list(zip(data['datetime'], data['PM2.5'])),
               columns = ['datetime', 'pm2_5'])
df = df.sort_values(by='datetime')
df.to_csv('./app/data/fimi02_new.csv', index=False)