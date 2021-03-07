# 7.2 函数简介 & 定义

# 应该使用有实际含义的名称来命名函数（增加代码可读性）
def greet_user():              # 用一个末尾的冒号表示：我们定义了一个代码块
    print('Hi there!')         # 在这个缩进水平下的语句——属于这个函数
    print('Welcome aboard')


print("Start")     # 更好的格式：在定义完一个函数后空两行
greet_user()       # 调用函数：必须在定义函数之后才能调用它
print("Finish")

'''
运行结果：
----------------
Start
Hi there!
Welcome aboard
Finish
----------------
'''
