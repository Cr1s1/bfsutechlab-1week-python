# 7.3 参数

# 7.3.1 单个参数的函数
def greet_user(name):            # name为参数名
    print(f'Hi {name}!')         # 格式化的字符串
    print('Welcome aboard')


print("Start")           # 更好的格式：在定义完一个函数后空两行
greet_user("John")       # 调用函数并且传值
greet_user("Mary")       # 再次调用函数并传递另外一个值
print("Finish")

'''
运行结果：
-------------------
Start
Hi John!
Welcome aboard
Hi Mary!
Welcome aboard
Finish
-------------------
'''

print('\n')

# 7.3.2 多个参数的函数
def greet_user(first_name, last_name):            # 该函数有两个参数
    print(f'Hi {first_name} {last_name}!')        # 格式化的字符串
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")     # 此处应该传递两个值
print("Finish")

'''
运行结果：
----------------  
Start
Hi John Smith!
Welcome aboard
Finish
----------------
'''