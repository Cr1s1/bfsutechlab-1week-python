# 7.6 创建可重用函数
# 任务：使用函数重新组织期中小练习四中的代码（可重用的部分从第8行到第15行）
# 原因：这里代码实现的功能，可能需要应用到其他不同的程序中，而这些代码没有必要重复写

# part1：回顾小练习四中的代码
"""
message = input(">")           # 第7、16行的输入输出语句不需要包含在函数中
words = message.split(' ')
emojis = {
    ":)": "😀 ",
    ":(": "😟",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
"""

# part2：正式编写
def emoji_converter(message):     # 函数的形参，message是一个字符串变量
    words = message.split(' ')
    emojis = {
        ":)": "😀 ",
        ":(": "😟",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output    # 返回值是一个字符串


message = input(">")
result = emoji_converter(message)   # 将返回值赋给一个变量
print(result)
# print(emoji_converter(message))  也可以通过这样简化代码

