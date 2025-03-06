my_str="itheima itcast boxuegu"
count=my_str.count("it")
print(f"里面有{count}个it字符")

new_my_str=my_str.replace(" ","|")
print(f"替换后为{new_my_str}")

new_my_str=new_my_str.split("|")
print(f"替换后为{new_my_str}")