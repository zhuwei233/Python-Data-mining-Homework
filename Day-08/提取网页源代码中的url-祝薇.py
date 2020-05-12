"""
提取网页源代码中的url
作者：祝薇
"""
import re
import urllib.request
#STEP1 输入网址获得网页源代码，并写入html.txt
f1 = open('html.txt',"w+",encoding="UTF-8")
htp = str(input("请输入网址："))
f2 = urllib.request.urlopen(htp)
html = f2.read()
html = html.decode("utf-8")
print(html,file=f1)
f1.close()
#STEP2 从html.txt中提取url（可以直接print,也可以写入新的txt储存）
f1 = open('C:/Users/zhuwe/Desktop/html.txt',"r",encoding="UTF-8")
str = f1.read()
url = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
"""
url正则表达式参考原文链接：
https://blog.csdn.net/qq_25384945/article/details/81219075
"""
match = re.findall(url,str)
for i in match:
    print(i)
f1.close()
