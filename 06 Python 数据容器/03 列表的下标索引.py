# 列表中所有数据类型都可以存储
name1_list=["张馨月",700,52.2,True]
name2_list=[["张馨月",162,110],["程思旭",177,140]]
print(name1_list[1])
print(type(name1_list))
print(name2_list[1])
print(name2_list[1][1])

# 使用下标索引不要超出范围
# 正向取出从0开始
# -1 表示倒数第一个元素  -2 表示倒数第二个
print(name2_list[-1][-3])

