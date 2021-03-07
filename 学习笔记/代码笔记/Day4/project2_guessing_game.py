# 小练习二：制作猜谜游戏（运用while循环）
# 涉及知识点：变量重命名，变量类型转换，if语句，while循环
secret_number = 9
guess_count = 0                    # 原本这一行是 i = 0
#【变量重命名】选中变量，单击右键，点击reactor->rename选项，即可一次性对整个程序中的同一个变量重命名
# 重命名后的变量名guess_count，与原来的i相比较，使代码更具有可读性
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))  # 一个整数类型变量
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break                      # 【break语句】终止循环
else:
    print('Sorry, you failed!')

'''
运行结果举例1:
-----------------------
Guess: 1
Guess: 2
Guess: 3
Sorry, you failed!
-----------------------
运行结果举例2:
-----------------------
Guess: 9
You won!
-----------------------
'''
