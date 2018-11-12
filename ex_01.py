# 列表

# 1、定义
name_list = ["zhangsan", "lisi", "wangwu"]

# 2、取值和取索引
print(name_list[0])
# index由已知数据求得列表索引
print(name_list.index("wangwu"))

# 3、修改
name_list[1] = "李四"
print(name_list)

# 4、增加

# append在末尾追加
name_list.append("wangxiaoer")
print(name_list)

# insert插入
name_list.insert(1, "wangchao")
print(name_list)

# extend在末尾追加一个列表
temp_list = ["大师兄", "二师兄"]
name_list.extend(temp_list)
print(name_list)

# 5、删除
# remove删除指定数据
name_list.remove("wangchao")
print(name_list)

# pop默认删除列表最后一个元素
name_list.pop()
print(name_list)
name_list.pop(2)
print(name_list)

# del关键字删除列表元素
del name_list[1]
print(name_list)

# clear清空
temp_list.clear()
print(temp_list)

# 6、列表统计
# len得到列表长度
print(len(name_list))

# count得到列表某一元素个数
print(name_list.count("zhangsan"))

# 7、排序

# sort升序
num_list = [4, 5, 6, 1, 3, 8, 4, 10]
print(num_list)
num_list.sort()
name_list.sort()
print(num_list)
print(name_list)

# 降序
num_list.sort(reverse=True)
print(num_list)

# reverse逆序（反转）
name_list.reverse()
print(name_list)

# 8、循环遍历for
for num in num_list:

    print(num)
