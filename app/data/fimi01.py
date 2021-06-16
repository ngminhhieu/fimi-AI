import requests
import pandas as pd
from datetime import datetime
import os

startTs = str(int(datetime.timestamp(datetime(2021, 5, 12, 15, 40, 0))*1000))
endTs = str(int(datetime.timestamp(datetime(2021, 5, 12, 16, 40, 0))*1000))

auth_token='eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI5ZjU2ZWMzMC1lMTNkLTExZWEtOWE1Zi1kN2MxMTYzZGQzZjMiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOWVlYTQ3YjAtZTEzZC0xMWVhLTlhNWYtZDdjMTE2M2RkM2YzIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjIzNzgzNjA5LCJleHAiOjE2MjM3OTI2MDl9.u9C2qGcn8WSQOzmP3PA-_hyf0cQmb_PwPdnQhzK3F5SUXEHtpiEq4gzImBA5nRQhBuu5oY_gkjHOgPU851K1kg'
headers = {'X-Authorization': 'Bearer ' + auth_token}
params = {'limit' : 10000,
        'startTs': startTs,
        'endTs': endTs,
        'keys': 'PM2_5'}

device_type = "DEVICE"
device_id = "d3aafd20-a6fc-11eb-8131-efbcb50b4b8d"
url = 'http://45.77.243.33:8080/api/plugins/telemetry/{}/{}/values/timeseries'.format(device_type, device_id)
response = requests.get(url, params=params, headers=headers)
data = response.json()
date = []
pm2_5 = []
for i in range(len(data['PM2_5'])):
    ticks = data['PM2_5'][i]['ts']
    date.append(datetime.fromtimestamp(float(ticks)/1000))
    pm2_5.append(data['PM2_5'][i]['value'])

df = pd.DataFrame(list(zip(date, pm2_5)),
        columns = ['datetime', 'pm2_5'])
df = df.sort_values(by='datetime')
df.to_csv('./app/data/fimi01_new.csv', index=False)

