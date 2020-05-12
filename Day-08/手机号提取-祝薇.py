"""
手机号提取
作者：祝薇
"""
if __name__ =="__main__":
    import re
    f1 = open('num.txt',"r",encoding="UTF-8")   #num是原始字符串
    f2 = open('call.txt',"w+",encoding="UTF-8") #call写入提取的电话号
    str = f1.read()
    phone_num = re.compile('13[0,1,2,3,4,5,6,7,8,9]|15[0,1,2,7,8,9,5,6,3]|18[0,1,9,5,6,3,4,2,7,8]|17[6,7]|147\d{8}')
"""
手机号正则表达式来源：CSDN博主「左手小兜」
原文链接：https://blog.csdn.net/weixin_42336574/article/details/89088999
移动：
134X(0-8)、135、136、137、138、139、150、151、152、157X(0-7\9)(TD)、
158、159、182 、183、184、187（3G\4G)、188(3G)147(数据卡）、178（4G）
联通：
130、131、132、155、156、185(3G)、186(3G) 、145(数据卡）、176（4G）
电信：
180(3G)、181(3G)、189(3G)、133、153、（1349卫通） 、177（4G）
"""
    match = phone_num.finditer(str)
    for i in match:
        print(i.group())
        print(i,file = f2)
    f1.close()
    f2.close()

