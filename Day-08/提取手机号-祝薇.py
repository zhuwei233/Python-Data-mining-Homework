"""
提取手机号
作者：祝薇
"""
if __name__ =="__main__":
    import re
    f1 = open('num.txt',"r",encoding="UTF-8")
    f2 = open('call.txt',"w+",encoding="UTF-8") #路径自行补充
    str = f1.read()
    phone_num = re.compile('1\d{10}')
    h = phone_num.finditer(str)
    for i in h:
        print(i.group())
        print(i,file = f2)
    f1.close()
    f2.close()

