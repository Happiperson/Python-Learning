# 列表的遍历：
def list_while_func():
    my_list=["陈思旭","程思旭","传智教育"]
    index=0
    while index<len(my_list):
        x=my_list[index]
        print(x)
        index+=1
list_while_func()

def list_for_func():
    my_list = ["陈思旭", "程思旭", "传智教育"]
    for x in my_list:
        print(x)
list_for_func()