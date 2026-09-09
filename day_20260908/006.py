# 里氏替换原则 LSP
# 子类可以替换父类，而不会改变程序的正确性
# 子类可以扩展父类的功能，而不会改变父类的正确性
# 子类可以重写父类的方法，而不会改变父类的正确性
# 子类可以添加新的方法，而不会改变父类的正确性

# 举例1 
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

# 正方形类
class Square(Rectangle):
    
    def set_height(self, height):
        self.height = height
        self.width = height
    
    def get_width(self, width):
        self.width = self.height
        self.height = self.width
# 假设有一个函数，它接受 Rectangle对象，并期望通过分别设置宽高来计算面积
def resize_and_calculate_area(rect: Rectangle):
    rect.set_width(4)
    rect.set_height(5)
    return rect.get_area()

rect = Rectangle(0, 0)
print(resize_and_calculate_area(rect))

sq = Square(0, 0)
print(resize_and_calculate_area(sq))
