# 完整的for循环
# 遍历字典的列的表

students=[
    {"name":"xiaoming"},
    {"name":"xiaohong",
     "age":18,
     "weight": 50},
    {"name":"zhangsan"}
]
find_name="xiaohongl"
for stu_dict in students:


    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        print(stu_dict)
        break
else:
    print("未找到")
print("循环结束")