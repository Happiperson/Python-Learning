# 通用操作 len max min
# 字典转不了，会去掉value
mylist=[1,2,3,4,5]
mytuple=(1,2,3,4,5)
mystr="12345"
myset={1,2,3,4,5}
mydict={"key1":1,"key2":2,"key3":3}

# len
print(f"列表里的元素有:{len(mylist)}")
# max
print(f"字典里的最大元素为:{max(mydict)}")
# min
print(f"字典里的最小元素为:{min(mydict)}")

# 容器的通用转换功能
# 容器转列表
print(f"列表转列表的结果为:{list(mylist)}")
print(f"元组转列表的结果为:{list(mytuple)}")
print(f"字符串转列表的结果为:{list(mystr)}")
print(f"集合转列表的结果为:{list(myset)}")
print(f"字典转列表的结果为:{list(mydict)}")
# 容器转元组
print(f"列表转元组的结果为:{tuple(mylist)}")
print(f"元组转元组的结果为:{tuple(mytuple)}")
print(f"字符串转元组的结果为:{tuple(mystr)}")
print(f"集合转元结果为:{tuple(myset)}")
print(f"字典转元组的结果为:{tuple(mydict)}")
# 容器转字符串
print(f"列表转字符串的结果为:{str(mylist)}")
print(f"元组转字符串的结果为:{str(mytuple)}")
print(f"字符串转字符串的结果为:{str(mystr)}")
print(f"集合转字符串的结果为:{str(myset)}")
print(f"字典转字符串的结果为:{str(mydict)}")
# 容器转集合
print(f"列表转集合的结果为:{set(mylist)}")
print(f"元组转集合的结果为:{set(mytuple)}")
print(f"字符串转集合的结果为:{set(mystr)}")
print(f"集合转集合的结果为:{set(myset)}")
print(f"字典转集合的结果为:{set(mydict)}")
# sorted排序   # 弄成列表
mylist=[3,1,2,4,5]
mytuple=(7,2,3,4,5)
mystr="12845"
myset={6,2,4,9,5}
mydict={"key1":8,"key2":2,"key3":1}
print(f"列表对象的排序结果：{sorted(mylist)}")
print(f"元组对象的排序结果：{sorted(mytuple)}")
print(f"字符串对象的排序结果：{sorted(mystr)}")
print(f"集合对象的排序结果：{sorted(myset)}")
print(f"字典对象的排序结果：{sorted(mydict)}")
# 反序
print(f"列表对象的排序结果：{sorted(mylist,reverse=True)}")
print(f"元组对象的排序结果：{sorted(mytuple,reverse=True)}")
print(f"字符串对象排序结果：{sorted(mystr,reverse=True)}")
print(f"集合对象的排序结果：{sorted(myset,reverse=True)}")
print(f"字典对象的排序结果：{sorted(mydict,reverse=True)}")