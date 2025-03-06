# 演示循环中断语句 continue
for i in range(1,6):
    print("a1")
    continue
    print("a2")

# 演示continue的嵌套应用
for i in range(1,6):
    print("b1")
    for i in range(1,6):
        print("b2")
        continue
        print("b3")
    print("b4")
print("b5")

# 演示break语句
for i in range(1,10):
    print("语句1")
    break  # 只要遇到break整个循环完蛋
    print("语句2")
print("语句3")