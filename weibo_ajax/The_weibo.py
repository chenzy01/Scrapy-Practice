from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient


base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers ={
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
client = MongoClient('mongodb://localhost:27017/')
db = client['weibo']     #指定数据库：weibo
collection = db['weibo'] #指定集合：weibo


#获取网页内容
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    #构造完整的url，urlencode()方法将参数转为URL的GET请求参数
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)

#解析爬取的内容
def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            #每页中index为1的信息不是所需的内容
            if index ==1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')  #微博的ID
                #借助pyquery将正文中的HTML标签去掉
                weibo['text'] = pq(item.get('text')).text() #正文
                weibo['attitudes'] = item.get('attitudes_count') #赞数
                weibo['comments'] = item.get('comments_count')   #评论数
                weibo['reports'] = item.get('reports_count')     #转发数
                yield weibo


def save_to_mongo(result):
    if collection.insert_one(result):
        print('Saved to Mongo')

if __name__ == '__main__':
    for page in range(1, 3):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)

'''
urlencode()用法
接受参数形式为：[(key1, value1), (key2, value2),...] 和 {'key1': 'value1', 'key2': 'value2',...} 
返回的是形如key2=value2&key1=value1字符串

enumerate()
函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
一般用在 for 循环当中()

PyQuery 的 text() 方法获取对应的文字

'''




