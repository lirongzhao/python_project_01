# 1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
a = [1, 2, '6', 'summer']
count = str(a.count('i'))
if count == 0:
    print('i没有出现在列表中')
else:
    print("i出现了{}次".format(count))

# 2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
dict_1 = {"class_id": 45, 'num': 20}
if dict_1["num"] > 5:
    print(dict_1['num'])
# 注：num表示课堂人数。如果大于5，输出人数。
# 3、list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
# 方法1： 手动扩充--字典--存放在列表里面；{} --简单
list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list1[0] = {'姓名': '肥兔', '性别': '男', '年龄': '18', '城市': '北京'}
list1[1] = {'姓名': '鹿鹿', '性别': '女', '年龄': '19', '城市': '深圳'}
list1[2] = {'姓名': 'Freestyle', '性别': '男', '年龄': '11', '城市': '湖南'}
list1[3] = {'姓名': '等', '性别': '男', '年龄': '12', '城市': '上海'}
list1[4] = {'姓名': '地球', '性别': '男', '年龄': '13', '城市': '广州'}
list1[5] = {'姓名': '阑珊', '性别': '女', '年龄': '14', '城市': '北京'}
list1[6] = {'姓名': '柠檬', '性别': '女', '年龄': '15', '城市': '北京'}
print(list1)
# 方法2： 自动--dict（）--不强制-- for循环 ，list.append() --- 难度
list2 = []
for i in list1:
   list2.append(dict(name=i, sex='男', age='18', city='北京'))
print(list2)
# 4、for循环遍历其他的数据类型 --字典
dict1 = {"name": "hcalb", "age": 18, "gender": "male"}
# 方法一：通过dict1.items()函数获取字典的所有键值对，然后再循环
for key, value in dict1.items():
    print(key, ":", value)
# 方法二
for key in dict1:
    print(key, ":", dict1[key])