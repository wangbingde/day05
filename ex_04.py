# 字符串
str1 = "hello python"

# 1、统计长度
print(len(str1))

# 2、统计某一个子字符串出现的次数
print(str1.count("llo"))
print(str1.count("abc"))

# 3、某一个字符串出现的位置
print(str1.index("llo"))

# 4、判断空白字符
str2 = "  \t\r\n"
print(str2.isspace())

# 5、判断字符串中是否只包含数字
str3 = "1"
print(str3.isdecimal())
print(str3.isdigit())
print(str3.isnumeric())

# 6、查找和替换
hello_str = "hello world"
# 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))
# 判断是否以指定字符串结束
print(hello_str.endswith("orld"))

# 查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("abc"))
# 替换字符串
print(hello_str.replace("world", "python"))
print(hello_str)

# 7、文本对齐
poem = ["登鹳雀楼",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"
        ]
for poem_str in poem:
    # 居中（使用中文全角空格）
    # print("|%s|" % poem_str.center(10,"　"))
    # 左对齐
    # print("|%s|" % poem_str.ljust(10,"　"))
    # 右对齐
    print("|%s|" % poem_str.rjust(10, "　"))

# 8、去除空白字符
poem2 = ["\t\n登鹳雀楼",
         "白日依山尽",
         "黄河入海流",
         "欲穷千里目\t\n",
         "更上一层楼"
         ]
print("")

# strip去掉string左右两边的空白字符
for poem2_str in poem2:
    print("|%s|" % poem2_str.strip().center(10, "　"))

# 9、拆分和拼接
poem_str3 = "登鹳雀楼\t 白日依山尽 \t 黄河入海流 \t\n 欲穷千里目 \t\t 更上一层楼"
print(poem_str3)

# 拆分字符串split
poem3 = poem_str3.split()
print(poem3)

# 合并字符串join
result = " ".join(poem3)
print(result)

# 10、字符串的切片
# 字符串【开始索引：结束索引：步长】
num_str = "0123456789"
# 2~5
print(num_str[2:6])
# 2~末尾
print(num_str[2:])
# 开始～5
print(num_str[:6])
# 截取完整字符串
print(num_str[:])
# 从开始处每隔1个字符截取
print(num_str[::2])
# 从1开始每隔一个
print(num_str[1::2])
# 从2开始到倒数第一个字符
print(num_str[2:-1])
# 得到末尾两个数字
print(num_str[-2:])
# 通过切片得到字符串的逆序
print(num_str[-1::-1])
print(num_str[::-1])
