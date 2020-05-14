import xlrd
import json
import os
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

cols = []
def json_to_excel(jsfile, excfile):
    a = 1
    if os.path.exists(jsfile):
        with open(jsfile, 'r',encoding='utf8') as fp:
            line = fp.readline()
            if not line:
                print("没有内容")
            else:
                jsdata = json.loads(line)
                for k in jsdata.keys():
                    if k not in cols:
                        cols.append(k)
                ws.append(cols) 
        with open(jsfile, 'r', encoding='utf8') as fp:
                while True:
                    print('正在写入的行数%s：' % a)
                    line = fp.readline()
                    if not line:
                        break
                    jsdata = json.loads(line)
                    rowdata = []
                    for col in cols:
                        rowdata.append(jsdata.get(col))
                    a += 1
                    ws.append(rowdata) 
    print('保存中')
    wb.save(excfile) 
if __name__ == '__main__':
    jsfile = "C:/Users/zhuwe/Desktop/聆听丶芒果鱼直播间时间切片弹幕.json"
    excfile = "C:/Users/zhuwe/Desktop/text.xlsx"
    json_to_excel(jsfile, excfile)

 

