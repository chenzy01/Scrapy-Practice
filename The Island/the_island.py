import requests
import pandas as pd
import numpy as np
import json
from requests.exceptions import RequestException
import time

base_url = "http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset="

#获取数据，爬取每一页的评论
def crawl_every_page_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
        #请求页面信息
        response = requests.get(url, headers=headers)
        #页面访问不成功，返回空值
        if response.status_code == 200:
            json_response = response.json()
            #return json_response
            #json_response = response.content.decode()
            #data = response.text
            #json_response = json.loads(data)
            #返回一个字典
            return json_response
        return None
    except RequestException:
        return None

#处理数据，解析每一个结果
def parse(html):
    #data = json.loads(html)['cmts']
    #result = []
    # 影评数据在 cmts 这个 key 中
    comments = html.get("cmts")
    if not comments:
        return None

    for itme in comments:
        yield {
            'id': itme['id'],       #影评id
            'time': itme['time'],     #影评时间
            'score': itme['score'],    #影评得分
            'cityName': itme['cityName'], #影评城市
            'nickName': itme['nickName'], #影评人昵称
            'gender': itme['gender'] if 'gender' in itme else '0',   #影评人性别，1表示男性，2表示女性
            'content': itme['content'].replace('\n', '', 10)   #影评内容
        }
#开始抓取数据，爬取影评
def crawl_film_review(total_page_num=100):
    data = []
    for i in range(1,total_page_num + 1):
        #构造爬取的地址，间隔1
        url = base_url + str(i)
        crawl_data = crawl_every_page_data(url)
        time.sleep(0.5)
        if crawl_data:
            data.extend(parse(crawl_data))
    return data

if __name__=='__main__':
    columns = ['id', 'time', 'score', 'city', 'nickname', 'gender', 'content']
    df = pd.DataFrame(crawl_film_review(1000), columns=columns)
    print("Done")
    #将性别映射后的数字转为汉子
    df['gender'] = np.where(df.gender==1,"男性", "女性")
    #根据id去除重复影评
    df = df.drop_duplicates(subset=['id'])

    df.to_csv('《一出好戏》影评_1000.csv', index=False)
    #df = pd.read_csv("《一出好戏》影评_1000.csv", encoding=gbk)






