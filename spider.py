# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup
import random
import requests
import pandas as pd
from sqlalchemy import create_engine
import time

engine = create_engine('mysql+pymysql://root:123456@localhost/tzqc?charset=utf8mb4')

agent1 = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'
agent2 = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0'
agent3 = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31'
agent4 = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'
agent5 = 'Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.15'
agent6 = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0'
list = [agent1, agent2, agent3, agent4, agent5, agent6]
agent = random.choice(list)
header = {
    'User-Agent': agent
}


def get_page_index(url):
    response = requests.get(url, headers=header).text
    data = re.findall('onclick="javascript:detail_tzqc\(\'(.*)\'\);">', response)
    get_detail_page(data)
        # print(url)


def get_detail_page(data):
    # a = time.strftime("%Y-%m-%d ", time.localtime())
    # outputfile = 'D:/PIC/' + a + '.xls'
    # writer = pd.ExcelWriter(outputfile)
    for data in data:
        url = 'https://cctvtzqc.com/tzqc/variety?acc=' + data
        response = requests.get(url, headers=header).text
        b=data
        data = re.findall('\["(.*?)","(.*?)","(.*?)","(.*?)"\]', response)
        name = ['品种', '1', '品种盈亏', '成交量']
        data = pd.DataFrame(columns=name, data=data)
        data.to_excel(writer, b)
        writer.save()
        # data.to_excel(outputfile,sheet_name=a)
    # a=time.strftime("%Y-%m-%d ", time.localtime())
    # data.to_sql('tct', engine, index=False, if_exists='append')


a = time.strftime("%Y-%m-%d ", time.localtime())
outputfile = 'D:/PIC/' + a + '.xls'
writer = pd.ExcelWriter(outputfile)
for page in range(4):
    url1 = {
        'fields': 'integral',
        'group': '1',
        'page': page + 1,
        'rows': '20'
    }
    url = 'https://cctvtzqc.com/tzqc/rank?' + urlencode(url1) + '&kw='
    get_page_index(url)

