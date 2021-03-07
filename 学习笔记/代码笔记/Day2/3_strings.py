 # 3.字符串

# 3.1 字符串的引号使用（单引号、双引号、三引号）
course1 = 'Python for Beginners'               # 1)单引号
course1 = "Python for Beginners"               # 2）双引号
course2 = "Python's Course for Beginners"      # 3）必须使用双引号的情况
course3 = 'Python for "Beginners"'             # 4）必须使用单引号的情况
course4 = '''
Hi John,

Here is our first email to you.

Thank you, 
The support team
'''
print(course1)
print(course2)
print(course3)
print(course4)
'''
运行结果：
--------------------------------
Python for Beginners
Python's Course for Beginners
Python for "Beginners"

Hi John,

Here is our first email to you.

Thank you, 
The support team
---------------------------------
'''

# 3.2 在字符串中索引字符
# 3.2.1 在字符串中索引一个字符，并且提取出来（类似于C语言的数组）
course = 'Python for Beginners'
first = course[0]            # 脚标从零起，0表示第一个字符的位置
second = course[1]           # 脚标1表示第二个字符
last = course[-1]            # 使用负数可以从后往前索引，-1就是倒数第一个字符（负几--倒数第几）
print('first = ' + first)
print('second = ' + second)
print('last = ' + last)
print(course[-2])            # -2可以检索到倒数第二个字符
print('\n')                  # \n是换行符
'''
运行结果：
--------------------
first = P
second = y
last = s
r

--------------------
'''

# 3.2.2 在字符串中索引（连续的）多个字符，并且提取出来（用方括号、冒号）——复制一整个或部分的字符串
course = 'Python for Beginners'
print('输出前几个字符：' + course[0:3])      # 脚标从0起
print('输出前几个字符：' + course[:5])       # 默认从第一个字符开始
print('默认输出整个字符串：' + course[:])
print('排除前几个字符：' + course[2:])       # 默认索引到最后一个字符
print('从中间截取几个字符：' + course[7:10])
print('从第几个到最后一个：' + course[4:-1] + '\n')
another = course[:]
print('another = ' + another)             # 变量another可作为变量course的副本
'''
运行结果：
-----------------------
输出前几个字符：Pyt
输出前几个字符：Pytho
默认输出整个字符串：Python for Beginners
排除前几个字符：thon for Beginners
从中间截取几个字符：for
从第几个到最后一个：on for Beginner
another = Python for Beginners

-----------------------
'''

# 3.2.3 小练习：思考下面的语句的运行结果
name = 'Jennifer'
print(name[1:-1])
'''
运行结果：
------------
ennife
------------
原因：索引序号从0起。因此冒号左边的索引为1，表示从第二个字符开始索引并包含该字符。
     冒号右边是-1，表示索引到最后一个字符截止，但并不包含该字符
'''

# 3.3 格式化的字符串
first = 'John'
last = 'Smith'
# 希望在终端打印出： John [Smith] is a coder （会用到”+“加号连接字符串）
message1 = first + ' [' + last + '] is a coder'     # 方法一：看上去比较复杂，结果不可视化
message2 = f'{first} [{last}] is a coder'           # 方法二：格式化的字符串，输出更加可视化
print(message1)
print(message2)
'''
运行结果：
--------------------------
John [Smith] is a coder
John [Smith] is a coder
--------------------------
'''

# 3.4.1 len函数计算字符串的长度
course = 'Python for Beginners'
print(len(course))
length = len(course)
print(length)
'''
运行结果：
---------
20
20
---------
'''

# 3.4.2 几个特定于字符串的函数（方法）
# 3.4.2.1 upper方法：将所有字母转换成大写
course = 'Python for Beginners'
print(course.upper())
print(course)                 # 原字符串没有被修改
'''
运行结果：
-----------------------
PYTHON FOR BEGINNERS
Python for Beginners
-----------------------
'''

# 3.4.2.2 lower方法:将所有字母转换成小写
course = 'Python for Beginners'
print(course.lower())         # 2)lower方法:将所有字母转换成小写
print(course)                 # 原字符串没有被修改
'''
运行结果：
-----------------------
python for beginners
Python for Beginners
-----------------------
'''

# 3.4.2.3 find方法：查找指定字符/字符串，返回在原字符串中第一次出现的索引
course = 'Python for Beginners'
print(course.find('P'))
print(course.find('o'))             # 第一次出现o的位置对应的索引是4
print(course.find('O'))             # 原字符串中不存在O，所以返回-1
print(course.find('Beginners'))     # 字符串Beginners从索引11开始（开头字母B对应的索引B）
'''
运行结果：
-----------
0
4
-1
11
-----------
'''

# 3.4.2.4 replace方法：替换字符或字符序列
course = 'Python for Beginners'
print(course.replace('Beginners', 'Absolute Beginners'))       # 字符序列的替换
print(course.replace('P', 'J'))                                # 字符的替换
print(course.replace('beginners', 'Absolute Beginners'))       # 查找不到被替换的字符/字符序列，输出原字符串
print(course)                                                  # 原字符串没有被修改
'''
运行结果：
---------------------------------
Python for Absolute Beginners
Jython for Beginners
Python for Beginners
Python for Beginners
---------------------------------
'''

# 3.4.2.5 in运算符：检查字符或字符序列中是否包含某指定字符或字符序列，并返回一个布尔值
course = 'Python for Beginners'
print('Python' in course)             # 使用in运算符，检查原字符串中是否包含Python
is_in = 'Python' in course            # 可以将返回结果赋值
print(is_in)
print('python' in course)             # in运算符大小写敏感
'''
运行结果：
-----------
True
True
False
-----------  返回的结果是布尔值
'''