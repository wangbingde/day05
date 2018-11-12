# 元组

# 1、定义
info_tuple = ("zhangsan", 18, 1.75)
print(info_tuple[1])
single_tuple = (5,)
print(type(single_tuple))

# 2、count
print(info_tuple.count(18))

# 3、index
print(info_tuple.index(18))
print(len(info_tuple))

# 4、循环遍历
for item in info_tuple:
    print(item)

# 5、格式字符串
info = ("zhangsan", 18)
print("%s的年龄是 %d 岁" % info)
# 拼接
info_str = "%s的年龄是 %d 岁" % info
print(info_str)

# 6、元组和列表的转换tuple(列表)和list(元组)
num_list=[1,2,3,4,5]
num_tuple=tuple(num_list)
print(type(num_tuple))
num2_list=list(num_tuple)
print(type(num2_list))
