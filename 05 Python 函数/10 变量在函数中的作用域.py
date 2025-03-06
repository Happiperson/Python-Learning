# 局部变量 全局变量
num=200
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num   # 设置内部定义的变量为全局变量
    num=500
    print(f"test_b:{num}")
test_a()
test_b()
print(num)