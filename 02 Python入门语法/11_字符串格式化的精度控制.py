# 精度控制的语法 %m.n
num=11.345
print("宽度限制%2.3f"%num)
print("宽度限制%2f"%num)
print("宽度限制%2d"%num)
print("宽度限制%2.1f"%num)
print("宽度限制%1.0d"%num)#m自身比数还小，默认没有用
#小数部分会四舍五入
print("宽度限制%2.2f"%num)
cha="李析东个人爬"
print("宽度限制%20s"%cha)

