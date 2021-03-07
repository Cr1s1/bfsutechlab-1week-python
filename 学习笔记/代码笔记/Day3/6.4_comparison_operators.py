# 6.4 比较运算符

# 6.4.1 大于运算符 “＞”
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
'''
运行结果：
--------------------
It's not a hot day
--------------------
结论：第一个表达式“temperature > 30”的布尔值为假
'''
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
'''
运行结果：
--------------------
It's a hot day
--------------------
结论：第一个表达式“temperature > 30”的值为假
'''

# 6.4.2 小于运算符“＜”
temperature = 35
if temperature < 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# 6.4.3 等于运算符“==”
temperature = 35
if temperature == 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# 6.4.4 不等于运算符“!=”
temperature = 35
if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# 6.4.5 大于等于运算符“>=”
temperature = 35
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# 6.4.6 小于等于运算符“＜=”
temperature = 35
if temperature <= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# 6.4.7 小练习：假设有一个输入字段，供用户输入他们的名字，编写程序提供输入提示来限制用户输入名字的长度。
'''
需要实现的逻辑：
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters 
otherwise
    name looks good!
'''
# 可以尝试每次输入不同长度的名字观察输出结果的不同
name = input('What is your name? ')  # 可回看第二章第二节input函数复习
print(len(name))

if len(name) < 3:  # 检查长度下限
    print('Name must be at least 3 characters.')
elif len(name) > 50:  # 检查长度上限
    print('Name can be a maximum of 50 characters.')
else:
    print('Name looks good!')
'''
运行结果1：
---------------------------------------
What is your name? J
1
Name must be at least 3 characters.
---------------------------------------
运行结果2：
---------------------------------------
What is your name? BFSUer
6
Name looks good!
---------------------------------------
运行结果3：
-----------------------------------------------------------------------------------------------------------
What is your name? 1iuegwhjdsfgoeqiwdhxs2w4q3456789o87654323ryuedrftgyhujkmdsghjvbnfgh34567890ertyuizxcvb
86
Name can be a maximum of 50 characters.
------------------------------------------------------------------------------------------------------------
'''
