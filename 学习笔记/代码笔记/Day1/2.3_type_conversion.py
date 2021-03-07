# 2.3 变量类型转换 & 获取变量类型

# 2.3.1 变量类型转换的用法（以字符串转换为整数为例）
birth_year = input('Birth year: ')
age = 2021 - int(birth_year)
print(age)
'''
运行结果：
--------------------
Birth year: 1982
39
--------------------
'''

# 2.3.2 常见的三种变量类型转换
age = '39'
int(age)              # 1)字符串转换为整数
rating = '4.9'
float(rating)         # 2）字符串转换为浮点数
is_old = 'True'
bool(is_old)          # 3）字符串转换为布尔值

# 2.3.3 type()函数，获取变量类型
birth_year = input('Birth year: ')
print(type(birth_year))                # 调用type函数，将返回结果用print输出
age = 2021 - int(birth_year)
print(type(age))
'''
运行结果：
-------------------
Birth year: 1982
<class 'str'>
<class 'int'>
-------------------
结论：变量birth_year是字符串类型，变量age是整数类型
'''

# 2.3.4小练习：向用户询问体重多少磅，并将其换算成千克，然后输出(千克 = 磅*0.45)
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
'''
运行结果：
--------------------
Weight (lbs): 160
72.0
--------------------
'''