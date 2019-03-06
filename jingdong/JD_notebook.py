from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo
import time

'''
爬取京东笔记本电脑信息
'''
#连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.JD_products
collection = db.products

#启动浏览器
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 50)


#存储数据信息
def to_mongodb(data):
    try:
        collection.insert(data)
        print("Insert The Data Successfully")
    except:
        print("Insert The Data Failed")

def serch():
    browser.get('https://www.jd.com/')
    try:
        #查找搜索框和搜索按钮，输入信息并点击按钮
        input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button")))
        input[0].send_keys('笔记本')
        submit.click()
        #查找笔记本按钮及销量按钮，依次点击按钮
        button_1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_selector > div:nth-child(2) > div > div.sl-value > div.sl-v-list > ul > li:nth-child(1) > a")))
        button_1.click()
        button_2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_filter > div.f-line.top > a:nth-child(2)")))
        button_2.click()
        #获取总页数
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > em:nth-child(1) > b")))
        return page[0].text
    except TimeoutException:
        search()
























