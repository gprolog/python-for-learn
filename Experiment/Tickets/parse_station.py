#查询所有的车站信息  如果要将信息保存到文件 命令：python parse_station.py > station.py

import re
import requests
from pprint import pprint
url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
response=requests.get(url,verify=False)
stations=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(stations),indent=4)
