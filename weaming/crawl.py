"""
https://sz.meituan.com/meishi/b751/rating/pn3/
"""
import sys
import requests
from data_process.io_csv import write_csv

cookies = {
    '_ga': 'GA1.2.907367213.1569410351',
    'client-id': '55f48872-0b82-4d24-8592-8d9bde7d8b31',
    'uuid': '9d9fff2a-af72-49fb-b0c7-6f9f9ed80982',
    '_lxsdk_cuid': '16dfc0ca8bec8-079150f24abed6-38647b00-384000-16dfc0ca8be3d',
    '_lxsdk': '16dfc0ca8bec8-079150f24abed6-38647b00-384000-16dfc0ca8be3d',
    'ci': '30',
    'rvct': '30%2C1',
    '__mta': '49631641.1571891820128.1571891820128.1571891820128.1',
    '_hc.v': '74df4ea7-2762-6175-ff6a-28d650ad13e0.1571892105',
    'lat': '22.53342',
    'lng': '113.921883',
    '_lxsdk_s': '16dfc0ca8bf-7f9-a2c-6e3%7C%7C38',
}

headers = {
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache',
    'Referer': 'https://sz.meituan.com/meishi/b751/rating/pn3/',
    'Connection': 'keep-alive',
}


def get_page(page):
    params = (
        ('cityName', '\u6DF1\u5733'),
        ('cateId', '0'),
        ('areaId', '751'),
        ('sort', 'rating'),
        ('dinnerCountAttrId', ''),
        ('page', str(page)),
        ('userId', ''),
        ('uuid', '9d9fff2a-af72-49fb-b0c7-6f9f9ed80982'),
        ('platform', '1'),
        ('partner', '126'),
        ('originUrl', 'https://sz.meituan.com/meishi/b751/rating/pn3/'),
        ('riskLevel', '1'),
        ('optimusCode', '10'),
        (
            '_token',
            'eJyVT8uuokAQ/ZfeQuwGGhB3V7mAKCoiKJm4aKV5iCLSgFcm8+/TN+MsZjlJJefUqcep+gmaeQImEkIGQiLoaQMmQBqhkQZE0DJeUXVpbMiaghRDFsH5Xw1jQwSnJjLB5IesakjUET5+K1su/FEkjNFRfHNFHx9FGfP47przJpC3bc0mELJhdKNF25FqdL7fIOcsL+BJVyXYkLaoMlhXCuRX/c+ADAE3uu24EcfyjeSN7d/c40/zzazIKs6o+7xeSmn9HD78nMIgP9C6/AqIzcqlNA2DmJ2nbv+Jnd1BQIfCm9pp/nnPLBe7Q+w5jzTuFWOJEs9bmMzYtPdp7J9WRZPTnTTzl6TShI0Ok40a5LbqrB8hVa3OicJXuciv1epF5gl1CYnwZdUbxSJ4qcpe3aO0XGxnymxca97p6ld15zCUWRZNMLIbc9YT/9nt68Y0qbVVP6DtZl8oDPVSwFnbXcK2YKmxi/xe6EkRVeZhTdeGo3nTTawkF7gaVnDnSltZGPuH9DHsqzP0lzMSWS/w6zdbUacq',
        ),
    )

    response = requests.get(
        'https://sz.meituan.com/meishi/api/poi/getPoiList',
        headers=headers,
        params=params,
        cookies=cookies,
    )
    try:
        return response.json()
    except Exception as e:
        print(e, response.text)
        sys.exit(1)


data = []
for page in range(1000):
    page_data = get_page(page)['data']['poiInfos']
    if page_data:
        data += page_data
        print(f'got page {page}')
    else:
        break

write_csv(data, './SZ.csv')
