# 元组可以存放任何数据类型
# 和列表的区别，中括号改成了小括号，且不可改变
# 定义元组
t1=(1,2.5,"张馨月",False)
t2=()
t3=tuple()
print(f"数据类型为{type(t1)},数据元素有{t1}")
print(f"数据类型为{type(t2)},数据元素有{t2}")
print(f"数据类型为{type(t3)},数据元素有{t3}")
# 定义单个元素的元组
t4=("张馨月",)
print(f"数据类型为{type(t4)},数据元素有{t4}")
# 元组的嵌套
t5=((1,2,3,3),(8,7,9,3))
print(f"数据类型为{type(t5)},数据元素有{t5}")
# 下标索引去取出内容
print(f"取出元素为{t5[0][2]}")

t6=("张馨月","张馨月","陈思旭")
# 元组的操作：index查找方法
index=t6.index("张馨月")
print(f"index查找结果为{index}")
# 元组的操作：count统计方法
print(f"count查找结果为{t6.count(3)}")
# 元组的操作：len函数统计元组元素数量
lenth=len("张馨月")
print(f"len找结果为{lenth}")
# 元组的遍历：while
index=0
while index<len(t6):
    print(t6[index])
    index+=1

# 元组的遍历:for
for i in t6:
    print(t6)

# 元组不可修改，但是可以在元组里面嵌套一个列表，这样就可以改了
t9=(1,2,[50,60])
print(t9[2][0])
print(t9)
t9[2][0]=80
print(t9[2][0])
print(t9)