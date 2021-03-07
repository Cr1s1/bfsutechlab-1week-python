# 4.6 字典 dictionaries

# 4.6.1 定义一个字典
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# 4.6.2 访问字典中的每一项（使用方括号）
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
'''
运行结果：
----------------
John Smith
----------------
'''
# print(customer["birthday"])    访问一个不存在的键，会报错
# print(customer["Name"])        键名的大小写输入错误，也会报错

print('\n')

# 4.6.3 get方法(1)：访问字典中的每一项，且不用担心报错
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("name"))
print(customer.get("Name"))
print(customer.get("birthdate"))
'''
运行结果：
----------------
John Smith
None
None
----------------
'''

# 4.6.4 get方法（2）：访问不存在的键名时，提供默认项，不会获得None值
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("name"))
print(customer.get("birthdate", "Jan 1 1980"))
print(customer)

print('\n')

# 4.6.5 更新字典中的值（使用方括号）
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer["name"])
'''
运行结果：Jack Smith
'''

# 4.6.6 添加新的键值对（使用方括号）
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
'''
运行结果：Jan 1 1980
'''

# 4.6.7 小练习：将阿拉伯数字转换成英文单词
phone = input("Phone: ")
# 运用字典，将每一个阿拉伯数字映射到对应的英文单词上
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
'''
运行结果：
--------------------------------
Phone: 123456
One Two Three Four Five Six 
--------------------------------
'''