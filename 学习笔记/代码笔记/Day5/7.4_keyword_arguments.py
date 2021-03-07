# 7.4 关键字参数

# 7.4.1 关键字参数的格式
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')        # 格式化的字符串
    print('Welcome aboard')


print("Start")
greet_user(last_name="Smith", first_name="John")     # 这样是可以的
print("Finish")

# 7.4.2 同时使用时，关键字参数要放在位置参数的后面，反之会报错
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')     # 格式化的字符串
    print('Welcome aboard')


print("Start")
greet_user("Smith", first_name="John")        # 这样是可以的
print("Finish")

