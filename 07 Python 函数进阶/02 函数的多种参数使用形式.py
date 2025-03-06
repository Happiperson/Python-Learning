def use_info(name,age,gender):
    print(f"姓名是{name},年龄是{age},性别是{gender}")
# 位置参数
use_info("张馨月",20,"女")
# 关键字参数
use_info(name="程思旭",age=20,gender="男")
use_info(age=50,name="程小军",gender="男")  # 顺序可以随便打乱
use_info("程小军2",age=50,gender="男")    # 两个混用,但位置参数必须在前面
# 缺省参数（默认值）
# 默认值必须放到最后
def use_info(name,age,gender="男"):
    print(f"姓名是{name},年龄是{age},性别是{gender}")
use_info(name="程思旭1",age=20)  # 默认就是男
use_info("张馨月",20,"女")  # 改了就是女
# 不定长 - 位置不定长 *号
# 不定长定义的形式参数会作为元组存在，接受不定数量的参数传入
def use_info(*args):
    print(f"args参数的类型是{type(args)},内容是{args}")
use_info("张馨月啦啦啦",20,"女",123,12.5)
# 不定长 - 关键字不定长 **号
def use_info(**kwargs):  # 必须给KV型的
    print(f"args参数的类型是{type(kwargs)},内容是{kwargs}")
use_info(name="张馨月wuwuwu",age=20,gender="女",num=123)