#!/usr/bin/env python3
# Author    : weaming
# Mail      : garden.yuen@gmail.com
# Created   : 2019-10-24 12:58:27
import requests
from data_process.io_csv import read_csv

data = read_csv('./SZpure.csv')
print(data)
for x in data:
    value = f"{x['avgScore']} | {x['title']} | {x['address']} | ￥{x['avgPrice']}"
    res = requests.get(f'https://kv.drink.cafe/sadd/lunch/{value}')
    print(res.json())
