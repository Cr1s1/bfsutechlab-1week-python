# 4.3 列表方法
# 4.3.1 append方法：在列表末尾添加一个新项
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
'''
运行结果：
---------------------
[5, 2, 1, 7, 4, 20]
---------------------
'''

# 4.3.2 insert方法：在指定位置插入一个新项
numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)        # 前一个数是索引，后一个是待插入的数字
print(numbers)
numbers.insert(2, 20)
print(numbers)
'''
运行结果：
---------------------------
[10, 5, 2, 1, 7, 4]
[10, 5, 20, 2, 1, 7, 4]
---------------------------
'''

print('\n')

# 4.3.3 remove方法：删除列表中的一项
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)
'''
运行结果：
-------------------
[2, 1, 7, 4]
-------------------
'''

# 4.3.4 clear方法：清空整个列表
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)
'''
运行结果：
---------
[]
---------
'''

# 4.3.5 pop方法：删除列表中的最后一个元素
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)
'''
运行结果：
---------------
[5, 2, 1, 7]
---------------
'''

# 4.3.6 index方法：检查列表中是否存在一个元素
numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))      # 如果存在，返回的是该元素的索引
# index方法的局限：如果该元素不存在，会报错
'''
运行结果：0
'''

# 4.3.7 in操作符：检查一个元素是否存在与列表中
numbers = [5, 2, 1, 7, 4]
print(50 in numbers)
print(5 in numbers)
'''
运行结果：
--------
False
True
--------
'''

# 4.3.8 count方法：计算值相同的元素在列表中出现的次数
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))
'''
运行结果：2
结论：该列表中，5这个数字出现了2次
'''

# 4.3.9 sort方法：对列表按值的大小升序排列
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()     # 无参数，无返回值
print(numbers)
'''
运行结果：
--------------------
[1, 2, 4, 5, 5, 7]
--------------------
'''
# 4.3.10 reverse方法：逆序输出列表
numbers = [5, 2, 1, 5, 7, 4]
numbers.reverse()
print(numbers)
# 与sort方法结合，可以按值大小对列表降序排列
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)
'''
运行结果：
---------------------
[4, 7, 5, 1, 2, 5]
[7, 5, 5, 4, 2, 1]
---------------------
'''

print('\n')

# 4.3.11 copy方法：拷贝一个列表，生成一个新副本
numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()     # numbers和numbers2是两个独立的列表
numbers.append(10)
print(numbers2)               # 对原列表的操作不会影响到副本numbers2
'''
运行结果：
---------------------
[5, 2, 1, 5, 7, 4]
---------------------
'''

# 4.3.12 小练习：删除列表里的重复项
# 本部分涉及到if语句和for循环的知识，可以在学习完第五章（在第三天）相关知识后再回看本部分
numbers = [2, 2, 4, 6, 3, 4, 6, 1]   # 这个数字列表里面有很多重复项
uniques = []                         # 将新的列表初始化为空列表
# 通过循环将numbers中的每个值一一与uniques中的比对，如果第uniques中没有，就加入uniques
for number in numbers:
    if number not in uniques:
        uniques.append(number)    # 将该数字加入到新列表的末尾
print(uniques)
'''
运行结果：
------------------
[2, 4, 6, 3, 1]
------------------
结论：在新列表uniques中，原表的重复项被删除了
'''