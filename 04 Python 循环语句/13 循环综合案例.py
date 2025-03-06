# 使用循环对员工依次发工资
# continue跳过员工，break直接结束发工资
money=5000
for i in range(1,21):
    import random
    score=random.randint(1,10)
    if score<5:
        print(f"员工{i}绩效分{score}，不满足，不发工资，下一位")
        # continue跳过发工资
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i}获得工资1000元，公司余额{money}元")
    else:
        print(f"公司没钱了，下个月再来，快滚")
        break
