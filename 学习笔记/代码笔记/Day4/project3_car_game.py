# 小练习三：制作汽车游戏
# 涉及知识点：字符串方法，if语句，while循环

command = ""       # 初始化为空字符串，用于存放用户输入的指令
started = False    # 存储车子状态信息，防止用户重复“开车”或“停车”
while True:
    command = input('> ').lower()
    # 直接在接收到的字符串上使用字符串方法，这样以后command变量接收到的字符串都会转化为小写

    if command == 'start':
        if started:                                 # 提醒用户不要重复启动车子
            print('Car is already started!')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:                             # 提醒用户不要重复停车
            print('Car is already stopped!')
        else:
            started = False
            print('Car stopped.')
    elif command == 'help':
        print('''start - to start the car
stop - to stop the car                             
quit - to exit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that!")    # 思考：为什么这里不能使用单引号？

'''
运行结果举例：
---------------------------------
> help
start - to start the car
stop - to stop the car                             
quit - to exit
        
> ghj
Sorry, I don't understand that!
> stop
Car is already stopped!
> Start
Car started...
> start
Car is already started!
> stop
Car stopped.
> stop
Car is already stopped!
> quit
---------------------------------
'''
