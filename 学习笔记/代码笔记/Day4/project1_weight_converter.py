# 小练习一：重量单位转换器
# 用户可以以千克或磅为单位输入体重，然后由程序将其转换为另一个单位

weight = int(input('Weight: '))               # 思考1：为什么要用int函数？
unit = input('(L)bs of (K)g: ')

if unit.upper() == 'L':                       # 使之大小写不敏感（老师的方法）
    converted = weight * 0.45
    print(f'You are {converted} kilos.')
elif unit == 'K' or 'k':                      # 使之大小写不敏感（另一种方法）
    converted = weight / 0.45
    print(f'You are {converted} pounds.')
else:
    print("Wrong input!")

# 思考2：上述第7、10行两种方法分别是怎么做到让程序大小写不敏感的？
'''
运行结果1：
-------------------------
Weight: 160
(L)bs of (K)g: l
You are 72.0 kilos.
-------------------------
运行结果1：
-------------------------
Weight: 72
(L)bs of (K)g: k
You are 160.0 pounds.
-------------------------
'''