import re
func = re.compile(r'[a-zA-Z\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
def check_email(addr):
    if func.match(addr):
        print("邮箱地址正确")
    else :
        print('邮箱地址错误')
your_email = input('请输入邮箱地址：')
result = check_email(your_email)
