import random
num=random.randint(1,100)

# 通过一个布尔类型的变量，判断循环是否继续的标志
flag=True
i=1
while flag:
    guess=int(input("请输入你要猜的数"))
    if guess==num:
        print(f"您在您第{i}次的猜测后猜对")
        flag=False
    else:
        if guess<num:
            print(f"在您第{i}次的猜测中，您猜的数过小")
            i+=1
        else:
            print(f"在您第{i}次的猜测中，您猜的数过大")
            i+=1


