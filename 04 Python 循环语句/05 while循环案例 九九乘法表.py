i=1         #\t对齐
while(i<10):
    j=1
    while(j<=i):
        print(f"{j}*{i}={i*j}\t",end='')
        j+=1
    i+=1
    print()  #空内容就是换行