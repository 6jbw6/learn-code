# 面向对象的设计原则 
# SOLID 原则 
# S:Single Responsibility Principle 单一原则
# O:Open-Closed Principle 开放-关闭原则
# L:Liskov Substitution Principle 里氏替换原则
# I:Interface Segregation Principle 接口隔离原则
# D:Dependency Inversion Principle 依赖倒原则

#1. srp 单一原则
# 一个类只负责一个功能，不能负责多个功能
#2. 使用场景
#a 一个类做太多的事情：既能解析数据又能分析计算数据，入库
#b 修改一个功能时另外一个功能也会受到影响
#c 类会变得很大，难以阅读
#d 测试困难

# 举例1
from ast import main
class Journal:

    def __init__(self):
        self.entries = []

    # 添加条目
    def add_entry(self, text):
        self.entries.append(text)
        print(f"添加条目：{text}")

    # 删除条目
    def remove_entry(self, index):
        del self.entries[index]
        print(f"删除条目：{index}")

    # 保存到文件
    def save_to_file(self):
        print("保存到文件")

    # 上传到远程服务器  
    def upload_to_remote(self):
        print("上传到远程服务器")
# 发现问题
# 1. 保存的格式是文本格式，而不是JSON格式
# 2. 上传到远程服务器时，可能时FTP, SFTP, HTTP等

# 举例2 
# 职责拆分
# 1. Journal 只负责管理日记内容
# 2. FileStorage 类负责保存内容
# 3. RemoteStorage 类负责上传到远程服务器

# Journal 类
class Journal:
    pass
# FileStorage 类
class FileStorage:
   pass
# RemoteStorage 类
class RemoteStorage:
    pass

# 测试
if __name__ == "__main__":
    # 数据操作
    journal = Journal()
    journal.add_entry("I went for a walk")
    journal.add_entry("I ate a pizza")
   
    # 保存到文件
    file_storage = FileStorage("journal.txt")
    file_storage.save(journal)

    # 上传到远程服务器
    remote_storage = RemoteStorage()
    remote_storage.upload(journal)
# 总结
# 一个类/函数只负责一个功能，不能负责多个功能
# 好处
# 1. 类的职责清晰，易于维护
# 2. 类的代码量较少，易于理解
# 3. 类的测试更方便
