# 不使用内置函数len()，来统计字符串的长度
str1="I love Zhang Xinyue!"
str2="I love you!"
count=0
for i in str1:
    count+=1
print(f"该字符串的长度为{count}")

def my_len(data):
  count=0
  for i in data:
      count+=1
  print(f"该字符串的长度为{count}")
my_len(str1)
my_len(str2)
