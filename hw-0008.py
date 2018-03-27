# 一个HTML文件,找出里面的正文

from bs4 import BeautifulSoup
import requests


url = 'http://mil.news.sina.com.cn/china/2017-04-05/doc-ifycwymx3854291.shtml'
page = requests.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(str(page.text), 'html.parser')
article = soup.select('.content')[0].text


print(article)
