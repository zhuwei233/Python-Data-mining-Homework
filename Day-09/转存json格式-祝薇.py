import json

with open('C:/Users/zhuwe/Desktop/聆听丶芒果鱼直播间时间切片弹幕.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    print('这是文件中的json数据：',json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))
f = open('C:/Users/zhuwe/Desktop/text.txt',"w+",encoding="UTF-8")
print(json_data,file=f)
f.close()
