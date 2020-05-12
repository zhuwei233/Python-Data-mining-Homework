import json
test = ['111','222']
filename='test.json'
with open(filename,'w') as file_obj:
    json.dump(test,file_obj)
