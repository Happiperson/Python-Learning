# 取出列表中的偶数
num=[1,2,3,4,5,6,7,8,9,10]
new_num=[]
def list_while_func():
    index=0
    while index<len(num):
        if num[index]%2==0:
            new_num.append(num[index])
        index+=1
    index2=0
    while index2<len(new_num):
        print(f"{new_num[index2]},")
list_while_func()

def list_for_func():
    for x in num:
        if x%2==0:
            new_num.append(x)
    for x2 in new_num:
        print(f"{x2},")


