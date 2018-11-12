# 字典

# 1、定义
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}
# 字典是无序集合，print输出顺序与定义顺序不一致
print(xiaoming)
print(xiaoming.keys())

# 2、取值 [k]
print(xiaoming["name"])

# 3、增加/修改
xiaoming["weight"] = 50
xiaoming["age"] = 20
print(xiaoming)

# 4、删除pop
xiaoming.pop("weight")
print(xiaoming)

# 5、统计键值对数量len
print(len(xiaoming))

# 6、合并字典update
temp_dict = {"weight": 50}
xiaoming.update(temp_dict)
print(xiaoming)

# 7、清空clear
temp_dict.clear()
print(temp_dict)

# 8、循环遍历（略有不同）
# k是每次循环获得的key的值
for k in xiaoming:
    print("%s-%s" % (k, xiaoming[k]))

# 9、字典列表组合
card_list = [
    {"name": "张三",
     "qq": 12345,
     "phone": 10086},
    {"name": "李四",
     "qq": 123456,
     "phone": 10085}
]
for card_info in card_list:
    print(card_info)
