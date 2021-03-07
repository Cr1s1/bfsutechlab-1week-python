# 4.5 序列解包
coordinates = (1, 2, 3)  # 想象1，2，3分别是x，y，z轴的坐标

# 1）普通思路:有重复性操作，代码较冗长
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# 2）python的解压缩思路（unpacking）
coordinates = (1, 2, 3)   # 可以应用于元组
coordinates = [1, 2, 3]   # 也可以应用于列表
x, y, z = coordinates     # unpacking：等价于第6到8行的功能
print(y)
'''
运行结果：2
'''