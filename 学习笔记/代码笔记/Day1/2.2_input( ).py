# 2.2 input函数

# 2.2.1 input函数的用法
name = input('What is your name? ')
print('Hi ' + name)
'''
运行结果：
--------------------------
What is your name? Mosh
Hi Mosh
--------------------------
'''

# 2.2.2 小练习：问两个问题，第一个是人的名字，第二个是那个人喜欢的颜色，最后根据用户输入，打印类似”Mosh likes blue.“这样的语句
name = input('What is your name?  ')
color = input('What is your favorite color?  ')
print(name + ' likes ' + color + '.')
'''
运行结果：
------------------------------------
What is your name?  BFSUer
What is your favorite color?  blue
BFSUer likes blue.
-------------------------------------
'''