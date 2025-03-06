# 上一个满足就不会再判断了
# 可以直接在判断语句中写定义

if(int(input("请输入您的身高"))<120):
    print("免费进入")
elif(int(input("请输入您的VIP等级1-5"))>3):
    print("免费进入")
elif(int(input("请告诉我今天几号"))==1):
    print("免费进入")
else:
    print("条件都不满足，请购票")