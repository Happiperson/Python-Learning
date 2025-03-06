# 公式： lambda 传入参数：函数体（一行代码）无法重复使用
def test(compute):
    result=compute(1,2)
    print(f"compute的类型为{type(compute)},结果为{result}")
test(lambda x,y:x+y)

