# 函数
# 函数定义 
def function_name():
    pass
# 函数的调用 
function_name()

# 函数的参数 
# 实参和 形参
# 实参： 调用函数时传递的参数值
# 形参： 函数定义时定义的参数变量
# 位置参数 ： 调用函数时，根据参数的顺序传递实参。
def stu_info(name, age, sex):
    # 自我介绍
    print(f'姓名：{name}，年龄：{age}，性别：{sex}')

# 调用函数时传递实参
stu_info('张三', 18, '男')

# 关键字参数 ： 调用函数时，根据参数的名称传递实参。
stu_info(age=18, name='张三', sex='男')

# 默认参数： 函数定义时，为参数指定默认值。
def stu_info(name, age, sex='男'):
    # 自我介绍
    print(f'姓名：{name}，年龄：{age}，性别：{sex}')

# 调用函数时传递实参
stu_info('张三', 18)
# 调用函数时传递实参
stu_info('张三', 18, '女')
# 调用函数时传递实参
stu_info('张三', 18, sex='女')

# 函数参数的常用技巧 
# 可变参数： 函数定义时，为参数指定可变数量的实参。
# 批量接受实参： 可以将多个实参打包成一个元组，传递给函数。
def stu_info(*args):
    # 自我介绍
    print(f'姓名：{args[0]}，年龄：{args[1]}，性别：{args[2]}')
# 调用函数时传递实参
stu_info('张三', 18, '男')
# 调用函数时传递实参
stu_info('张三', 18, '女')
# 调用函数时传递实参
stu_info('张三', 18, '女')
# 批量接受关键字参数： 可以将多个关键字参数打包成一个字典，传递给函数。
def stu_info(**kwargs):
    # 自我介绍
    print(f'姓名：{kwargs["name"]}，年龄：{kwargs["age"]}，性别：{kwargs["sex"]}')
# 调用函数时传递实参
stu_info(name='张三', age=18, sex='男')
# 调用函数时传递实参
stu_info(name='张三', age=18, sex='女')
# 调用函数时传递实参
stu_info(name='张三', age=18, sex='女')
# 批量接受关键字参数

# 不要将可变参数作为参数的默认值 
def append_value(value,items=[]):
    items.append(value)
    return items
# 调用函数时传递实参
print(append_value(1))
# 调用函数时传递实参
print(append_value(2))
# 调用函数时传递实参
print(append_value(3))
# 调用函数时传递实参
print(append_value(4))
print('#'*40)
def append_value(value,items=None):
    if items is None:
        items = []
    items.append(value)
    return items

# 调用函数时传递实参
print(append_value(1))
# 调用函数时传递实参
print(append_value(2))
# 调用函数时传递实参
print(append_value(3))
# 调用函数时传递实参
print(append_value(4))
