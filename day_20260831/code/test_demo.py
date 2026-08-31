# 计算 圆的周长与面积 
# author: 123
# date: 2026-08-31
# version: 1.0

# 圆的周长 函数
def circle_perimeter(radius):
    """
    计算 圆的周长
    :param radius: 圆的半径
    :return: 圆的周长
    """
    return radius * 2 * 3.14

# 圆的面积 函数
def circle_area(radius):
    """
    计算 圆的面积
    :param radius: 圆的半径
    :return: 圆的面积
    """
    return radius ** 2 * 2

# 调用 圆的周长 函数
print(circle_perimeter(5))
# 调用 圆的面积 函数
print(circle_area(5))
