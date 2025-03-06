# 序列是指：内容连续、有序，可使用下标索引的一类数据容器
# 切片：从一个序列中，取出一个子序列
# 语法：序列[起始下标:结束下表：步长]
# 步长可以为负，代表反过来

my_list=[0,1,2,3,4,5,6]
result1=my_list[0:7:1]
print(f"结果1为{result1}")

my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[1:4]
print(f"结果2为{result2}")

my_str="0123456"
result3=my_str[::]
result4=my_str[::-1]
result5=my_str[::2]
print(f"结果3为{result3}")
print(f"结果4为{result4}")
print(f"结果5为{result5}")


