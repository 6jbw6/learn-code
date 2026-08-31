# 1.注释 
# 代码注释
user_input = 'xxxx'
# 用户输入用户名，并过滤空格
username = user_input.strip()
# 使用strip()去除空格
# 1. 数据库保存空间更小
# 2. 不必在代码中添加空格判断
username = user_input.strip()
# 2. 文档 
# 功能文档
def remove_invalid(s):
    """
    移除字符串中的无效字符
    :param s: 输入的字符串
    :type s: str
    :return: 移除无效字符后的字符串
    """
    pass
# 接口文档
class Person:
    """
    人类
    :param name: 姓名
    :type name: str
    :param age: 年龄
    :type age: int
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age
# 3. 用注释屏蔽代码
# 4. 标注注释写法
# 调用strip()去掉空格  X
# 如果直接把带空格的输入传递给后端，可能会导致服务崩溃 √
# 因此使用strip()方法去掉空格 √
username = user_input.strip()
