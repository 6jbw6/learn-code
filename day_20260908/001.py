# 类
# 面向对象编程OOP
# 基于类来创建对象，每个对象都自动具备类中的通用行为
# 根据类来创建对象：实例化 使用类的实例
# 1. 创建和使用类 
class Dog:
    
    # 初始化方法  当对象被创建时，自动调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"初始化方法被调用，{self.name}被创建了")

    def sit(self):
        print("狗在坐")

    def roll_over(self):
        print("狗在打滚")


#2. 根据类创建实例
my_dog = Dog("旺财", 3)
# 调用属性
print(my_dog.name)
print(my_dog.age)
# 调用方法
my_dog.sit()
my_dog.roll_over()

