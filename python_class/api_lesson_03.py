# python控制流&字典&列表
"""
python经典数据类型： int float bool str
列表:list []
1/列表里面可以存放任意数据类型(包括列表)，元素和元素之间用英文逗号隔开
2.列表统计元素个数：len()
3.取值：每个元素都有自己的位置--索引，从0开始
  取多个值：切片
扩展：列表里的嵌套，如何取值?list1[][]
4、列表元素可以被改变：增加元素，删除元素，修改元素
5、列表元素是可以重复的
元组，字典，集合
python控制流：
if判断，for循环
"""
list1 = [20, "zlr", True, 3.14, [1, 2, 3, 4]]   # 定义了一个空列表
# print(list1)
# print(len(list1))
# print(list1[1])
# print(list1[0:3])
# print(list1[4][2])
# 增加
# print(list1)
# list1.append("等")  # 追加到末尾
# print(list1)
# list1.insert(3, "露露")   # 指定位置进行追加
# print(list1)
# list1.extend(["地球", "阑珊", "柠檬"])  # 列表合并，可以同时添加多个元素
# print(list1)
# # 删除
# list1.pop(5)  # 默认删除最后一个元素 可以指定元素的索引进行删除
# print(list1)
# list1.remove(20)   # 删除指定元素
# print(list1)
# # list1.clear()   # 清空列表
# # print(list1)
# # 修改--进行重新赋值
# list1[0] = "飞兔"
# list1[1] = "飞兔"
# list1.append("飞兔")
# print(list1)
# print(list1.count("飞兔"))  # 统计列表中某个元素个数
"""
元组：tuple
1、元组里面可以存放任意数据类型(包括列表)，元素和元素之间用英文逗号隔开
2.元组统计元素个数：len()
3.取值：每个元素都有自己的位置--索引，从0开始
  取多个值：切片
扩展：元组里的嵌套，如何取值?list1[][]
**4、元组元素不可以被改变
5、元组元素是可以重复的
扩展：想要改变元组元素？-- 转成列表，就可以修改了,修改后再改为元组类型
"""
# tuple1 = (20, "zlr", True, 3.14, [1, 2, 3, 4])
# print(tuple1)
# list2 = list(tuple1)
# print(list2)
# list2[0] = '简单'
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)

"""
字典：dict{} 
1.元素是键值对的格式：key:value   --一个键值对是一个元素，多个元素之间用逗号隔开
2.字典一般的使用场景：描述一个物件的属性 ==人的属性：名字，年龄，性别
3.取值：通过key 来取value值 ==2个方法 dict1["key"] dict1.get("key")
注意：字典在3.6版本之前是没有顺序的，没有索引的
4.key的要求：1）是不可变的（不可以是可变的数据类型，比如列表，字典），2）key 不可以是重复的 
  value没有任何要求，可以被改变的（增加，删除，修改的操作）
5.统计元素个数--len
"""
# dict1 = {"name": "hcalb", "age": 18, "gender": "male"}   # 空字典
# print(dict1["age"])
# print(dict1.get("name"))
# print(dict1.keys())  # 取出键名
# print(dict1.values())  # 取出值
# print(dict1.items())   # 取出键值对
# 增加&修改  -- 加一个键值对
# dict1["hobby"] = "女"   # 如果key不存在，就是新增加一个键值对
# print(dict1)
# dict1["gender"] = "女"  # 如果key存在，就是更新key的值
# print(dict1)
# # 增加多个键值对？ dict1.update({})
# dict1.update({"city": "深圳", "weight": "130", "hight": "180"})
# print(dict1)
# 删除 --指定key进行删除
# dict1.pop("hobby")
# print(dict1)
# # 统计键值对个数
# print(len(dict1))
"""
集合：set  {},元素是单个的
1.集合元素是不能重复的  == 使用场景给列表去重
2.无序的
"""
# list3 = [22, 11, 11, 33, 44, 55]
# # # 获取列表里出现过的元素 -- 去重
# # print(list3)
# # set1 = set(list3)  # 强转为集合
# # list4 = list(set1)
# # print(list4)

"""
控制流：if判断 for循环 
if判断语法：
if 条件：  ----判断这个条件成立进入下面的执行语句--分支
    子代码（执行语句）
elif 条件：  ----可以没有，也可有多个
    子代码（执行语句）
elif 条件：
    子代码（执行语句）
else: ---没有条件的
    子代码（执行语句）
# """
# money = int(input("你有多少钱:"))
# if money >= 200:
#     print("做生意！")
# elif money >= 100:
#     print("买房子~")
# elif money >= 50:
#     print("买车")
# elif money >= 20:
#     print("买点零食")
# else:
#     print("好好学习，好好打工")

"""
for循环：重复执行某一块代码
使用场景：遍历某些数据对象的元素的 --字符串，列表，元组，字典，集合
缩进里是循环体
问题1：循环次数由元素个数决定
问题2：如何控制循环 if 判断 continue break

for循环结合一起使用的一个内置函数：range(start,stop,step) --生成一个整数序列
start: 从谁开始，默认值--0开始
stop: 到谁结束 --不能省略  ==取头不取尾
step: 步长 默认为1
"""
# str1 = "我爱柠檬班"
# # count = 0
# # for i in str1:
# #     print(i)
# #     print("*"*20)
# #     count += 1
# #
# # print(count)
# # print(len(str1))
# list1 = [20, "zlr", True, 3.14, [1, 2, 3, 4]]   # 定义了一个空列表
# for name in list1:
#     if name == 3.14:
#         #  break  # 中断循环体
#         continue  # 跳出本次循环，继续下次循环
#     print(name)
# 自己做一下循环遍历元组和字典
# tuple1 = (20, "zlr", True, 3.14, [1, 2, 3, 4])
# for j in tuple1:
#     if j == "zlr":
#         continue
#     print(j)
#     print("&"*5)
# 使用循环遍历字典
# dict1 = {"name": "hcalb", "age": 18, "gender": "male"}   # 空字典
# # 通过dict1.items()函数获取字典的所有键值对，然后再循环
# for key, value in dict1.items():
#     print(key, ":", value)

# for num in range(0, 11, 2):
#     print(num)

"""
总结目前学到了哪些内置函数:
print(),input()
"""
dict2 = {"name": "ccc"}
dict3 = dict(name="ccc", age=8)
print(dict2)
print(dict3)