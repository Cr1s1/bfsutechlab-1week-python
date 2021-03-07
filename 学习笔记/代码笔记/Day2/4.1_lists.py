# 4.1 列表
# 4.1.1 定义一个列表
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']      # 用方括号定义一个列表，字符串元素需要用引号括起来
print(names)
'''
运行结果：
------------------------------------------
['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
------------------------------------------
'''

# 4.1.2 列表中单个元素的索引
# 相关知识点：可复习2.2字符串的索引
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])            # 用索引来访问单个元素（0索引第一项）
print(names[2])            # 2索引第（2+1）项
print(names[-1])           # -1索引最后一项
print(names[-2])           # -2索引倒数第二项
'''
运行结果：
----------
John
Mosh
Mary
Sarah
----------
'''

# 4.1.3 列表中对一系列元素的索引
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:])         # 只指定开始索引，就默认一直访问到末尾
print(names[2:4])        # 只访问开始索引所指项，不访问结束索引所指项
print(names[:4])         # 只指定结束索引，就默认从第一项开始访问
print(names[:])          # 开始和结束索引都不指定，默认访问所有项
print(names[0:])         # 默认访问所有项
print(names)             # 字符串的索引语句不会修改最初的列表
'''
运行结果：
-------------------------------------------
['Mosh', 'Sarah', 'Mary']
['Mosh', 'Sarah']
['John', 'Bob', 'Mosh', 'Sarah']
['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
--------------------------------------------
'''

print('\n')

# 4.1.4 修改原列表中的单个元素
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'       # 直接使用索引和赋值语句修改其值
print(names)
'''
运行结果：
----------------------------------------------
['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']
----------------------------------------------
'''
print('\n')

# 4.1.5 小练习：找出列表中的最大元素
# 注：本练习需要用到for循环、if语句的知识，可以待学完第五章相关知识后再回看本练习
numbers =[3, 6, 2, 10, 8, 4]
max = numbers[0]                # 存放最大值，初始化为列表第一项的值（假设第一项最大）

#  需要遍历这个列表，获取其中每一项的值，每一次迭代进行一次比较
for number in numbers:
    if number > max:
        max = number
print(max)
'''
运行结果：10
'''