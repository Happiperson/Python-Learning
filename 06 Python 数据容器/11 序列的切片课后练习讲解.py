my_str="万过薪月,员序程马黑来,nohtyP学"
new_my_str=my_str[::-1][9:14]
print(f"结果1：{new_my_str}")
new2_my_str=my_str[5:10][::-1]
print(f"结果2：{new2_my_str}")
new3_my_str=my_str.split(",")[1].replace("来","")[::-1]
print(f"结果3：{new3_my_str}")

