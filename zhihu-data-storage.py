import requests
from pyquery import PyQuery as pq

#爬取知乎“发现”页面的“热门话题”部分
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
#调用items()后，得到一个生产器
items = doc('.explore-tab .feed-item').items()
#pyquery爬取的内容以字符串形式输出
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    #find('.content').html(),将 class='content'节点内的HTML文本提取，再从中提取纯文本
    anwser = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, anwser]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

    #with open('explore.txt', 'a', encoding='utf-8') as f:
    #    fi.write('\n'.join([question, author, anwser]))
    #    f.write('\n' + '=' * 50 + '\n')



