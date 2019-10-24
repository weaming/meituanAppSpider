#!/usr/bin/env python3
# Author    : weaming
# Mail      : garden.yuen@gmail.com
# Created   : 2019-10-24 12:58:27
import json
import requests
from data_process.io_csv import read_csv

data = read_csv('./SZpure.csv')
print(data)
for x in data:
    res = requests.get(
        f'https://kv.drink.cafe/sadd/lunch/{json.dumps(x, ensure_ascii=False)}'
    )
    print(res.json())
