# 实现计算不同多边形的面积的功能
# 使用OCP原则
from abc import ABC, abstractmethod

# close 关闭修改
class Shape(ABC):
    # 定义多边形的接口规则
    @abstractmethod
    def area(self):
        pass

# 计算矩形面积
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# 圆形面积
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

# 统一使用这个抽象类
def calculate_area(shape: Shape):
    return shape.area()

# 测试
if __name__ == "__main__":
    rect = Rectangle(4, 5)
    circle = Circle(3)
    print(calculate_area(rect))
    print(calculate_area(circle))
