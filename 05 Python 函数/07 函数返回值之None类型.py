# None的用法
# 函数返回值
def say_hi():
    print("我是一个无返回值函数")

result=say_hi()
print(f"无返回值函数，返回内容是{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")
# None用于if判断
def check_age(age):
    if age>18:
        print("您是成年人可以进入")
        return "SUCCESS"
    else:
        return None
result=check_age(16)
if not result:
    print("未成年，不可以进入")
# None用于声明无初始内容的变量
name=None
print(f"name的内容为{name}")


