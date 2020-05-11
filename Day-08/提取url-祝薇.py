import re
import urllib.request
htp = str(input("请输入网址："))
f = urllib.request.urlopen(htp)
html = f.read()
html = html.decode("utf-8")
print(html)
str = 'html'
print(re.findall(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]',str))
