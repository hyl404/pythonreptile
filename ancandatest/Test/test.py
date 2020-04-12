#https://s.askci.com/stock/a/0-0?reportTime=2017-6-30&pageNum=2#QueryCondition
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import pandas as pd
#解析网页
data = []
for i in range(1,5):
    paras = {
        'reportTime': '2017-6-30',
        'pageNum': i
    }
    url = 'https://s.askci.com/stock/a/0-0?' + urlencode(paras)
    print(url)
#解析资源
    response = requests.get(url)
    html = response.text
#解析网页，提取需要的资源
    tb = pd.read_html(html)[3]
#   print(tb)


#     soup = BeautifulSoup(html)
#    # print(soup)
#     tr_list = soup.find_all('tbody')
#     for data in tr_list:
#         print(data.text.split())
# #保存数据
    data.append(tb)
df = pd.concat(data)
df.to_csv('2.csv')