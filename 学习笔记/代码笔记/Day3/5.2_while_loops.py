# 5.2 while循环

# 5.2.1 while循环基础
i = 1
while i <= 5:
    print(i)       # 属于while循环
    i = i + 1      # 属于while循环
print("Done")      # 不属于while循环
'''
运行结果：
----------
1
2
3
4
5
Done
----------
'''

# 5.2.2 利用while循环来打印一个三角形
i = 1
while i <= 5:
    print('*' * i)       # 属于while循环（可以重复字符串）
    i = i + 1            # 属于while循环
print("Done")            # 不属于while循环
'''
运行结果：
----------
*
**
***
****
*****
Done
----------
'''