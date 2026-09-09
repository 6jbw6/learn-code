# DIP 依赖倒置原则
# 依赖倒置原则是指，高层模块不应该依赖低层模块，而应该依赖抽象。
# 抽象不应该依赖具体实现，具体实现应该依赖抽象。

# 举例1 
class MySqlDatabase:

    def insert_user(self, username: str):
        print(f"将用户 {username} 插入到 MySQL 数据库中")

class UserService:
    def __init__(self, database: MySqlDatabase):
        self.db = MySqlDatabase()
    
    def register_user(self, username: str):
        self.db.insert_user(username)
        print(f"用户 {username} 注册成功")

# DIP
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def insert_user(self, username: str):
        pass

# 底层
# mysql 数据库实现
class MySqlDatabase(Database):
    def insert_user(self, username: str):
        print(f"将用户 {username} 插入到 MySQL 数据库中")
# postgresql 数据库实现
class PostgreSQLDatabase(Database):
    def insert_user(self, username: str):
        print(f"将用户 {username} 插入到 PostgreSQL 数据库中")

# 高层
class UserService:

    def __init__(self,db: Database):
        self.db = db
    
    def register_user(self, username: str):
        self.db.insert_user(username)
        print(f"用户 {username} 注册成功")


if __name__ == "__main__":
    # 使用mysql 
    mysql_service = UserService(MySqlDatabase())
    mysql_service.register_user("user1")
    # 使用postgresql 
    postgresql_service = UserService(PostgreSQLDatabase())
    postgresql_service.register_user("user2")
        

       
