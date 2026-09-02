# 异常与错误处理 
# 1. 异常的概念
# 异常是指在程序运行过程中，出现的错误或异常情况。
# 异常可以分为两种：
# 语法错误（Syntax Error）
# 运行时错误（Runtime Error）

userid_pic_api = "https://www.baidu.com/"
# 获取某某用户的头像
user_pic_result = print(
    userid_pic_api
    )
# 2. 异常的处理
# 异常的捕获
try:
    user_pic_result = print(userid_pic_apis)
# Exception 异常的类型，用于捕获所有异常
except Exception as e:  
    print("获取用户头像失败")
    print(e)
# python 中异常的种类
# 变量未定义：NameError
# 类型错误：TypeError
# 索引错误：IndexError
# 键值对错误：KeyError
# 除数为0：ZeroDivisionError
# 超出范围：OverflowError
# 内存溢出：MemoryError
# 语法错误：SyntaxError
# 运行时错误：RuntimeError
# 文件不存在：FileNotFoundError
# try:
#     print("请输入两个整数，我将计算它们的商")
#     answer = int(input("请输入一个整数：")) / int(input("请输入另一个整数："))
# except ZeroDivisionError:
#     print("除数不能为0")
# # else -- 当没有异常发生时，执行的代码块
# else:
#     print("两个整数的商为：", answer)

# 读取xxx文件 -- FileNotFoundError
TRAIN_DATA_FILE = 'data.txt'
# 读取文件 路径错误--文件不存在
try:
    with open(TRAIN_DATA_FILE, 'r') as f:
        pass
except FileNotFoundError:
    print("文件不存在")
else:
    print("文件存在")
# 无论是否发生异常，都执行的代码块
finally:
    print("finally")

# 异常处理操作，要精确的放在指定的位置
# 读取文件 路径错误--文件不存在
try:
    with open(TRAIN_DATA_FILE, 'r') as f:
        pass
except FileNotFoundError:
    print("文件不存在")
except Exception as e:  # --> 捕获所有异常
    print("异常：", e)
else:
    print("文件存在")
# 无论是否发生异常，都执行的代码块
finally:
    print("finally")