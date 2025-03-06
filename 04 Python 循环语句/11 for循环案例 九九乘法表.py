i=1
for i in range(1,10):
    for j in range(1,i+1):  # 通过i控制每一行有几个算式
            print(f"{i}*{j}={i*j}\t",end='')
    print()