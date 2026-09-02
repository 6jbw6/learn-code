# 迭代器 与 可迭代对象
# 迭代器
# 不是所有的对象都可以作为循环主体，只有可迭代对象才能作为循环主体。
# iter() 函数可以将可迭代对象转换为迭代器对象。 next() 函数可以获取迭代器对象的下一个元素。
# 以 python 内置数据类型为例，如列表、元组、字符串等。
# 可迭代的对象有：
# 列表、元组、字符串、字典、集合、文件对象等
test_list_1 = [1,2,3,4,5]
# 将列表转换为迭代器对象
test_list_2 = iter(test_list_1)
# 利用 next() 函数获取迭代器对象的下一个元素
n = next(test_list_2)

# 循环 
# while 循环 
# while 循环会不断执行直至循环条件不能得到满足 
# courrent_number = 1 
# while courrent_number <= 5:
#     print(courrent_number)
#     # 循环变量自增
#     courrent_number += 1

# 死循环 
# while True:
#     print('#'*40)
#     print('用户输入q退出')
#     # 指定条件，当条件满足时，跳出循环
#     quit_key= input("请输入：q退出")
#     if quit_key == "q":
#         print('用户输入q退出')
#         print('#'*40)
#         break
# 终止循环  break
# 继续循环  continue 跳过当前循环，继续下一次循环
# 1 - 100 跳过有4的数字 使用while循环
i = 0
while i <= 100:
    i += 1
    if i % 10 == 4 or i // 10 == 4:
        continue
        # 跳过当前循环，继续下一次循环
    print(i)
# 占用 pass
# i = 0 
# while i <= 100:
#     pass

# 提示词
def prompt():
    pass

# 模型调度
def model():
    pass

# 输出结果
def output():
    pass

