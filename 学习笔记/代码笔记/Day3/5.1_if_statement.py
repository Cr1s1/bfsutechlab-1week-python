# 5.1 判断语句：if语句

# 5.1.1 缩进的规则
is_hot = False
if is_hot:                           # 注意：冒号不能漏写！
    print("It's a hot day")          # 属于if语句
    print("Drink plenty of water")   # 属于if语句
print("Enjoy your day")              # 不属于if语句
'''
运行结果：Enjoy your day
'''

is_hot = True                        # 修改初始条件
if is_hot:                           # 注意：冒号不能漏写！
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")
'''
运行结果：
------------------------
It's a hot day
Drink plenty of water
Enjoy your day
------------------------
'''

# 5.1.2 if...else语句
is_hot = True

if is_hot:                           # 注意：冒号不能漏写！
    print("It's a hot day")
    print("Drink plenty of water")
else:                                # 注意：冒号不能漏写！
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")
'''
运行结果：
------------------------
It's a hot day
Drink plenty of water
Enjoy your day
------------------------
'''

is_hot = False                       # 修改初始条件

if is_hot:                           # 注意：冒号不能漏写！
    print("It's a hot day")
    print("Drink plenty of water")
else:                                # 注意：冒号不能漏写！
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")
'''
运行结果：
------------------------
It's a cold day
Wear warm clothes
Enjoy your day
------------------------
'''

print('\n')

# 5.1.3 if...elif...else语句
is_hot = False
is_cold = True                       # 增加初始条件

if is_hot:                           # 注意：冒号不能漏写！
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:                        # 注意：冒号不能漏写！
    print("It's a cold day")
    print("Wear warm clothes")
else:                                # 注意：冒号不能漏写！
    print("It's a lovely day")

print("Enjoy your day")
'''
运行结果：
------------------------
It's a cold day
Wear warm clothes
Enjoy your day
------------------------
'''

print('\n')
is_hot = False
is_cold = False                       # 修改初始条件

if is_hot:                            # 注意：冒号不能漏写！
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:                         # 注意：冒号不能漏写！
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")
'''
运行结果：
------------------------
It's a lovely day
Enjoy your day
------------------------
'''

print("\n")

# 5.1.4 小练习：计算买房的首付
'''
需要实现的逻辑：
Price of a house is $1M.
If buyer has good credit,
    they need to put down 10% 
Otherwise
    they need to put down 20%
Print the down payment
'''
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
'''
运行结果：
--------------------------
Down payment: $100000.0
--------------------------
'''