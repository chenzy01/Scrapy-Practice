import json

data = [{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-09"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1992-11-09"
}]

#print(type(str))
#loads()将json文本字符串转为JSON对象
#data = json.loads(str)
#print(data)
#print(type(data))

#dumps()将json对象转为文本字符串
with open('data.json', 'w') as f:
    #indent代表缩进字符个数
    f.write(json.dumps(data, indent=2))
#数据中若有中文，要要指定编码格式
#with open('data.json', 'w', encoding='utf-8') as f:
#    f.write(json.dumps(data, indent=2, ensure_ascii=False))


