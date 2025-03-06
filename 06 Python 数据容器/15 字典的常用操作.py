# 可以容纳多个数据，且不同类型
# 每一份数据是KeyValue键值对
# 不支持下标索引
# 可以修改
# 支持for循环，不支持while循环
my_dict={
    "张馨月":99,
    "程思旭":88,
    "袁艺":33
}
# 新增元素
my_dict["唐展展"]=150
print(f"第一个结果为:{my_dict}")
# 更新元素
my_dict["程思旭"]=1000
print(f"第二个结果为:{my_dict}")
# 删除元素
my_dict.pop("袁艺")
print(f"第三个结果为:{my_dict}")
# 清空元素
my_dict.clear()
print(f"第四个结果为:{my_dict}")
# 获取全部的Key keys
my_dict={
    "张馨月":99,
    "程思旭":88,
    "袁艺":33
}
keys=my_dict.keys()
print(f"字典的全部keys是:{keys}")

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 方式2：直接对字典进行for循环
for key1 in my_dict:
    print(f"字典的key是：{key1}")
    print(f"字典的value是：{my_dict[key1]}")
# 统计字典内的元素数量
lenth=len(my_dict)
print(f"元素数量为{lenth}")