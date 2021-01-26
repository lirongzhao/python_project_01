# 20210112-Python第四节课：Python的函数
# 1. 把字符串转成列表 - list()
str1 = "hello,world"
print(list(str1))
# 2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
sum1 = 0
for i in range(0, 100, 2):
    sum1 += i
print(sum1)
# 3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
def len1(num):
    if len(num) > 5:
        return True
    else:
        return False
num = "nihaoha"
if len1(num):
    print("True")
else:
    print("False")
# 4. 课堂笔记
