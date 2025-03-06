"""input(提示信息)
 要注意键盘无论输入什么类型的数据都是字符串
 如果需要非字符串，需要用数据类型转换
"""
print("Hello")
msg=input("请输入你的姓名")
print(f"欢迎你{msg}！")
print("尊贵的%s,您是我们的超级VIP"%msg)
num=input("请输入您的号码")
print(f"您的号码是{num}")
num=int(num)
print(f"您的号码是{num}")



