"""
邮箱地址
作者：祝薇
"""
if __name__ =="__main__":
    import re
    f1 = open('text.txt',"r")
    f2 = open('email.txt',"w+") 
    str = f1.read()
    eml =  r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'
    match = re.search(eml,str)
    if match:
        print(match.group())
        print(match,file = f2)
    f1.close()
    f2.close()
