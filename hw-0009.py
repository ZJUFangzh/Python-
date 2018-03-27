import re
import urllib.request

url = "https://adblockplus.org/zh_CN/acceptable-ads"

print('We will extract links from ' + url + ' :')


with urllib.request.urlopen(url) as response:
    content = response.read()
    try:
        content = content.decode('utf-8')
    except UnicodeDecodeError:
        content = content.decode('gbk')
    link_list = re.findall('''(?<=href=)["'](.[^"']+)["']''', content)
    i = 1
    for item in link_list:
        print('%d:' % i, item)
        i += 1
