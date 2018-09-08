import requests
import pandas as pd
import numpy as np

base_url = "http://m.maoyan/com/mmdb/comments/movie/1203084.json?_v_=yes&offset="

#爬取每一页的评论
def crawl_every_page_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    #请求页面信息
    response = requests.get(url, headers=headers)
    #页面访问不成功，返回空值
    if response.status_code != 200:
        return []
    return response.json()
#解析每一个结果
def parse(data):
    result = []
    comments = data.get("cmts")

    if not comments:
        return []

    for cm in comments:
        yield [
            cm.get['id'],       #影评id
            cm.get['time'],     #影评时间
            cm.get['score'],    #影评得分
            cm.get['cityName'], #影评城市
            cm.get['nickName'], #影评人昵称
            cm.get['gender'],   #影评人性别，1表示男性，2表示女性
            cm.get['content']   #影评内容
        ]
#爬取影评
def crawl_film_review(total_page_num=100):
    data = []
    for i in range(1,total_page_num + 1):
        url = base_url + str(i)
        crawl_data = crawl_every_page_data(url)
        if crawl_data:
            data.extend(parse(crawl_data))
    return data

if __name__=='__main__':
    columns = ['id', 'time', 'score', 'city', 'nickname', 'gender', 'content']
    df = pd.DataFrame(crawl_film_review(4000), columns=columns)
    #将性别映射后的数字转为汉子
    df['gender'] = np.where(df.gender==1, "男性","女性")
    #根据id去除重复影评
    df = df.drop_duplicates(subset=['id'])

    df.to_csv('《一出好戏》影评_1000.csv', index=False)
    df = pd.read_csv("《一出好戏》影评_1000.csv", encoding=gbk)








