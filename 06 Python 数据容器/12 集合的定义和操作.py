# 集合最主要特点：不支持重复
# 集合使用{}
# 集合不支持下标索引访问
# 跟列表一样可以修改
# while循环不行，只能支持for循环

# 定义集合
my_set={"张馨月","唐展展","程思旭"}
my_set_empty=set()
print(my_set,f"类型为{type(my_set)}")
print(my_set_empty,f"类型为{type(my_set_empty)}")

# 添加新元素
my_set.add("袁艺")
print(my_set)
my_set.add("张馨月")
print(my_set)

# 移除元素
print(f"移除前：{my_set}")
my_set.remove("袁艺")
print(f"移除后：{my_set}")

# 随机取出一个元素
element=my_set.pop()
print(f"取出的一个元素为:{element}")
# 清空集合
my_set.clear()
print(f"清空后:{my_set}")
# 取2个元素的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"取出差集后set3内容:{set3}")
print(f"取出差集后，原有set1内容:{set1}")
# 消除2个集合的差集，在集合1内，消除和集合2相同的元素
set1.difference_update(set2)
print(f"消除差集后，原有set1内容:{set1}")
print(f"消除差集后，原有set2内容:{set2}") # 不变
# 2个集合合并为1个
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(f"合并后为：{set3}")
print(f"合并后set1为：{set1}")
print(f"合并后set2为：{set2}")
# 统计集合元素数量
set1={1,2,3,1,2,4,5,6}
num=len(set1) # 集合是去重的
# 集合的遍历
# 集合不支持下标索引，不能用while循环，但可以用for
set1={1,2,3,4,5}
for element in set1:
    print(element)
