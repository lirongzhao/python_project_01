# name = 'fafal'
# gender = 'female'
# hobby = '柠檬'
# # 方法1
# print('''----{0}基本信息----
# name:{1}
# gender:{2}
# hobby:{3}
# '''.format(name, name, gender, hobby))
# # 方法2
# print('''----%s基本信息----
# name:%s
# gender:%s
# hobby:%s
# '''%(name, name, gender, hobby))
"""
字符串操作：
1.取值：每个元素都有位置--索引，从0开始
2.取多个值：切片 ==指定头:尾：步长 ==取头不取尾
头默认值：从0开始 尾默认值：最后 步长默认值：1
3.获取字符串长度：len()
4.常用方法 变量.
"""
str1 = 'hello lemomban'
# print(str1[4])
# print(str1[-1])  # 后往前取也可以
# print(str1[0:5:1])
# print(len(str1))
# print(str1[0:len(str1):2])
# 获取某个元素的索引
# print(str1.index('y'))   # 没有找到元素会报错，代码会停止执行
# print(str1.find('y'))  # 没有找到元素不会报错，返回-1，代码不会停止运行
# 统计个数
# print(str1.count('l'))
# 元素替换
# print(str1.replace('lemomban', 'Python'))
# name = input('请输入姓名:')
# age = int(input("请输入年龄："))
# sex = input("请输入性别:")
# print("""
# ********************
# 姓名：{}
# 性别：{}
# 年龄：{}
# ********************
# """.format(name, sex, name))
str1 = "python hello aaa 123123aabb"

print(str1[0:6:])
print("o a" in str1)
print('he' in str1)
print('ab' in str1)
print(str1.replace("python", "lemon"))
print(str1.find('aaa'))












