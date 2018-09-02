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


#解析库的使用
from lxml import etree
import html

'''
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
'''
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

