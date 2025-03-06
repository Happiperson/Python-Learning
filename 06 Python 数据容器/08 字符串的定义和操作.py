# 定义一个字符串，只可以存储字符串，
# 可以看成字符的容器，支持下标索引
# 字符串和元组一样，都无法修改
my_str="I love you for one thousand years"
# 通过下标索引取值
value1=my_str[3]
value2=my_str[-1]
print(value1,",",value2)
# index方法
index1=my_str.index("o")
print(f"下标索引的值为{index1}")
# replace方法  字符串.replace(字符串1，字符串2)全替换
new_my_str=my_str.replace("o","e")
print(f"经过replace后，为{new_my_str}")
# split方法  字符串.split(分隔符字符串)
new2_my_str=my_str.split(" ")
print(f"经过split后，为{new2_my_str}")
# strip方法  规整操作，去前后空格，去前后指定字符串
my_str="    I love you for one thousand years   "
new3_my_str=my_str.strip()
print(f"经过strip，清楚首尾空格后，为{new3_my_str}")
my_str="12I love you for 12one thousand years21"
new4_my_str=my_str.strip("12") # 这里12和21是一个意思
print(f"经过strip，清楚12后，为{new4_my_str}")
# 统计字符串中某字符串出现的次数
my_str="I love you for one thousand years"
count=my_str.count("o")
print(f"o出现的次数为{count}")
# 统计字符串的长度
lenth=len(my_str)
print(f"字符串的长度为{lenth}")
