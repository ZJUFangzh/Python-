import requests
from bs4 import BeautifulSoup

path = r'D:\Python-trying\Python-trying\pic\\'


def downloadPic(url):
    req = requests.get(url)
    imgName = path + url.split('/')[-1]
    with open(imgName, "wb") as f:
        f.write(req.content)


html = requests.get('http://tieba.baidu.com/p/2166231880').content
soup = BeautifulSoup(html, "html.parser")
for img in soup.find_all('img', {'class', 'BDE_Image'}):
    downloadPic(img['src'])
