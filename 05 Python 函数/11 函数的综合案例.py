money=5000
name=None
name=input("请输入您的姓名")
def query():
    global name
    global money
    print("--------查询余额--------")
    print(f"尊敬的{name}：\n您当前的余额为{money}元")

def saving():
    saving_money=int(input("请输入您要存款的金额"))
    global name
    global money
    money+=saving_money
    print("--------存款信息--------")
    print(f"尊敬的{name}：\n存款金额：{saving_money}\n存款成功！")
    query()

def giving():
    giving_money=int(input("请输入您要取款的金额"))
    global name
    global money
    if(giving_money>money):
        input("余额不足，按回车返回主页面")
        return None
    money-=giving_money
    print("--------取款余额--------")
    print(f"尊敬的{name}：\n取款金额：{giving_money}\n取款成功！")
    query()

i=None
for i in range(1,10):
    print("我们的服务：\n"
      "******1.查询******\n"
      "******2.存款******\n"
      "******3.取款******\n"
      "******4.退出******\n"
        "----------------")
    choice=int(input(f"尊敬的{name}：请通过按键进行操作！"))
    if(choice==1):
        query()
        i+=1
    elif(choice==2):
        saving()
        i+=1
    elif(choice==3):
        giving()
        i += 1
    elif(choice==4):
        break
    else:
        print("输入值非法!请重新输入！")
        i += 1
print("交易成功，请取走卡片！")


