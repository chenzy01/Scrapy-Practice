#抓取知乎网页，headers必须传递
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

import requests
#比较返回码和内置的成功返回码，requests.codes.not_found可以用来判断结果是不是404
r = requests.post("http://www.jangshu.com")
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

import requests
#上传文件，文件要和当前脚本在同一个目录下
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)

import requests
#维持同一个会话，而不用多次设置cookies。用于模拟登录成功之后再进行下一步操作
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


#添加verify参数控制检查是否检查证书，不添加的话默认为True
import requests
from requests.packages import urllib3
#import logging
#设置忽略警告，也可通过捕获警告到日志的方式忽略警告
urllib3.disable_warnings()
#logging.captureWarnings(True)
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

#身份认证
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
#直接传一个元祖，程序默认使用HTTPBasicAuth类进行认证
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)


#将请求表示为数据结构与浏览器交互
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'
}
s = Session()
req = Request('POST',url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)


#正则表达式
import re

content = 'Hello 123 4555 World_this I a REGEX demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

#贪婪匹配
content = 'Hello 123 4555 World_this I a REGEX demo'
print(len(content))
result = re.match('^He.*(\d+).*demo$', content)
print(result)
print(result.group(1))
#输出：7,因为.*会尽可能匹配更多字符，而.*后面是\d+,至少匹配一个数字

#非贪婪匹配
content = 'Hello 123 4555 World_this I a REGEX demo'
print(len(content))
result = re.match('^He.*?(\d+).*demo$', content)
print(result)
print(result.group(1))
#输出：1234567,因为.*?会尽可能少的匹配字符


#解析库lxml的使用
from lxml import etree
import html


text =
<div>
<ul>
<li class ="item-0"> <a href="link1.html" > first itme </a> </li>

<li class ="item-1"> <a href="link2.html" > second itme </a> </li>
<li class ="item-inactive"> <a href="link3.html" > third itme </a> </li>
<li class ="item-1"> <a href="link4.html" > forth itme </a> </li>
<li class ="item-0"> <a href="link5.html" > fifth itme </a> 
</ul>
</div>

#调用HTML类进行初始化，构造一个Xpath解析对象
#利用etree模块自动修复html
html = etree.parse('./text.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

#选取所有节点
result = html.xpath('//*')
#选取直接子节点a
result = html.xpath('//li/a')
#选取父节点，然后获取其属性
result = html.xpath('//a[@href="link4.html"]/../@class')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
#属性过滤
result = html.xpath('//li[@class="item-0"]')
#获取文本
result = html.xpath('//li[@class="item-0"]/a/text()') #逐层获取
result = html.xpath('//li[@class="item-0"]//text()') #获取子孙节点内部的所有文本
#获取属性
result = html.xpath('//li/a/@href')
#属性多值匹配
'''
text = <li class="li li-first"><a href="link.html">first time</a></li>
'''
result = html.xpath('//li[contains(@class, "li")]/a/text()')
#多属性匹配,用and操作符相连
'''
text = <li class="li li-first" name="item"><a href="link.html">first time</a></li>
'''
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
#按序选择
result = html.xpath('//li[1]/a/text()')
result = html.xpath('//li[last()]/a/text()')
result = html.xpath('//li[position()<3]/a/text()')


#BeautifulSoup库的使用

import html
from bs4 import BeautifulSoup


html = '''
<html>
<head><title>The Dormouse`s story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
    <span>Elsie </span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
'''
#初始化BeautifulSoup时，会自动更正不标准的HTML字符串
soup = BeautifulSoup(html, 'lxml')
prettify() 方法把要解析的字符串按标准格式进行缩进输出
print(soup.prettify())
print(soup.title.name)
print(soup.head)
#获取指定节点的直接子节点
print(soup.p.contents)
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i, child)
#获取所有子孙节点
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i, child)
#分别获取下一个和前一个兄弟节点
print(soup.p.next_sibling)
print(soup.p.previous_sibling)

#方法选择
html ='''
<div class="panel">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">foo</li>
<li class="element">bar</li>
<li class="element">jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">foo</li>
<li class="element">bar</li>
</ul>
</div>
</div>
'''
#find_all(name, attrs, recursive, text, **kwargs)
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
#根据节点名字查询元素
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
#根据属性查询元素,attrs参数的类型是字典
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
print(soup.find_all(class_='element'))


#pyquery 库的使用,基于CSS选择器

from pyquery import PyQuery as pq

html ='''
<div id="container">
<ul class="list">
<li class ="item-0">first itme</li>
<li class ="item-1"><a href="link2.html" >second itme</a></li>
<li class ="item-0 active"><a href="link3.html"><span class="bold">third itme</span></a></li>
<li class ="item-1 active"><a href="link4.html" >forth itme</a></li>
<li class ="item-0"><a href="link5.html">fifth itme</a> 
</ul>
</div>
'''

doc = pq(html)
print(doc('li'))
#初始化URL
doc = pq(url='http://cuiqingcai.com')
print(doc('title'))

print(doc('#container .list li'))
print(type(doc('#container .list li')))

items = doc('.list')
lis = items.find('li')
#获取子节点
lis = items.children('.active')
print(lis)
#遍历,调用items()后，得到一个生产器
lis = doc('li').items()
for li in lis:
    print(li, type(li))
#获取属性
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
#获取属文本
li = doc('li')
#html()返回第一个li节点内部的HTML文本，text()只返回所有纯文本内容
#attr(),text(),html(),三个方法若传入参数，则获取相应信息，传入参数，则对相应部分赋值
print(li.html())
print(li.text())



