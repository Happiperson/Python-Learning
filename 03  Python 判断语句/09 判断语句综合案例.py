import random
num=random.randint(1,10)
guess_num=int((input("输入你要猜测的数字: ")))
if(guess_num<num):
    input("您猜测的数字过小")
elif(guess_num==num):
    input("您猜对了，太牛了")
else:
    input("您猜测的数字过大")

guess_num = int((input("再次输入你要猜测的数字: ")))
if (guess_num < num):
    input("您猜测的数字过小")
elif (guess_num == num):
    input("您猜对了，太牛了")
else:
    input("您猜测的数字过大")

guess_num = int((input("第三次输入你要猜测的数字: ")))
if (guess_num < num):
    input("您猜测的数字过小，游戏失败")
elif (guess_num == num):
    input("您猜对了，太牛了")
else:
    input("您猜测的数字过大，游戏失败")