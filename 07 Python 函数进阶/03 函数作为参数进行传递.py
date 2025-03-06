def test(compute):
    result=compute(1,2)
    print(f"computer的类型为{type(computer)},结果为{result}")
def computer(x,y):
    return x+y
test(computer)
# 函数传入的作用在于：传入计算逻辑，而非传入数据