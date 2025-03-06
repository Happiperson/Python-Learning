# 键值对的Key和Value可以是任意类型
# Key不允许重复，重复添加等于覆盖
# 字典不可以选择下标索引，只能用Key

# 定义字典
my_dict={"张馨月":99,"程思旭":88,"袁艺":55}
# 定义空字典
my_dict2={}
my_dict3=dict()
print(f"字典1的内容是：{my_dict}，类型是{type(my_dict)}")
print(f"字典1的内容是：{my_dict2}，类型是{type(my_dict2)}")
print(f"字典1的内容是：{my_dict3}，类型是{type(my_dict3)}")
#定义重复Key的字典
my_dict={"程思旭":99,"程思旭":88,"袁艺":55}
print(f"字典1的内容是：{my_dict}")  # 覆盖了
# 从字典中基于Key获取value
my_dict={"张馨月":99,"程思旭":88,"袁艺":55}
score=my_dict["张馨月"]
print(f"张馨月考试分数为{score}")
# 定义嵌套字典
stu_score_dict={
    "王力宏":{
        "语文":120,
        "数学":110,
        "英语":100
    },
    "周杰伦":{
        "语文":150,
        "数学":140,
        "英语":150},
    "林俊杰":{
        "语文":130,
        "数学":115,
        "英语":130}
}
# 从嵌套字典中获取信息
score1=stu_score_dict["周杰伦"]["语文"]
print(score1)
