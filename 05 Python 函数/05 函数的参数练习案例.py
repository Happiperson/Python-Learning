def say_hi():
    print("欢迎你！\n请出示您的二十四小时核酸证明，并测量体温")
def check(temperature):
    if(temperature>37.5):
        print("在体温测量中，您的体温是%.1f，需要隔离"%(temperature))
    else:
        print("在体温测量中，您的体温是%.1f，体温正常"%(temperature))

say_hi()
temperature=int(input("请输入测量体温"))
check(temperature)
