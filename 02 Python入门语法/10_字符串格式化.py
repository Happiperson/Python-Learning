# 多个变量占位，要用括号括起来，并且要按顺序
stu_address="重庆图书馆"
stu_tel=110
message="我的地址是%s,我的电话是%s,有事情请联系我"%(stu_address,stu_tel)
print(message)

#****常用占位符****
name="陈思旭"
birth_year=2002
weight=130.5
my_message="我叫%s,我出生于%d,现在体重%f"%(name,birth_year,weight)
print(my_message)