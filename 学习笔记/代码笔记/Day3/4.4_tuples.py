# 4.4 元组

# 4.4.1 定义元组 & 访问元组中的元素
numbers = (1, 2, 3)     # 元组用圆括号定义
print(numbers[0])
'''
运行结果：1
'''

# （补充）4.4.2 list函数和tuple函数：元组和列表的相互转换
# 来修改元组里的值
x = ("apple", "banana", "cherry")
y = list(x)       # 1）list函数：元组转换成列表
y[1] = "kiwi"     # 可以修改列表（但不能修改元组）
x = tuple(y)      # 2）tuple函数：列表转换成元组
print(x)
'''
运行结果：
------------------------------
('apple', 'kiwi', 'cherry')
------------------------------
'''

# （补充）4.4.3 len函数：确定元组中有多少项
this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))       # 思考：上一次用到len函数的地方是哪一章节？
'''
运行结果：3
'''

# （补充）4.4.4 创建仅有一个项的元组
# 注：如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组
this_tuple = ("apple",)   # 是元组（不要忘了逗号！）
print(type(this_tuple))

this_tuple = ("apple")    # 不是元组
print(type(this_tuple))
'''
运行结果：
-------------------
<class 'tuple'>
<class 'str'>
-------------------
'''

# （补充）4.4.5 del关键字：完全删除元组
this_tuple = ("apple", "banana", "cherry")
del this_tuple

# print(this_tuple)  会报错，因为该元组已不存在。

# （补充）4.4.6 +运算符：合并两个或多个元组
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2     # 用+运算符直接对变量名操作
print(tuple3)
'''
运行结果：
-------------------------------
('a', 'b', 'c', 1, 2, 3)
-------------------------------
'''
