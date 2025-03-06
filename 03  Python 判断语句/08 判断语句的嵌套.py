# 通过缩进确定层级关系
if int(input("你的身高是多少"))>120:
    print("您的身高需要买票")
    print("但是如果你是三级VIP以上就不用买票")
    if int(input("您的VIP等级是"))>3:
        print("免费进入")
    else:
        print("抱歉，你等级不够，仍需买票")
else:
    print("免费进入")
