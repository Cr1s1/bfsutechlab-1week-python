# 7.5 return语句

# 7.5.1 有return语句的情况
def square(number):
    return number * number    # return语句


result = square(3)      # 返回到调用函数处的值，可以用一个变量来接收
print(result)
print(square(3))        # 更简洁的打印结果的语句

'''
运行结果：
-------
9
9
-------
'''

# 7.5.2 函数无返回值的情况：返回None值
def square(number):
    print(number * number)     # 先执行这一行


print(square(3))               # 后执行这一行（函数默认返回None值）
'''
运行结果：
---------
9
None
---------
'''
