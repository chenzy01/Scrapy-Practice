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

#比较返回码和内置的成功返回码，requests.codes.not_found可以用来判断结果是不是404
r = requests.post("http://www.jangshu.com")
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

#上传文件，文件要和当前脚本在同一个目录下
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)


