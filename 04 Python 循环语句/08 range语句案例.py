num=input("请输入你要查找0到多少以内的数")
num=int(num)
count=0
for x in range(num):
    if x%2==0:
        count+=1
print(f"在您需求的集合内，有{count}个偶数")

