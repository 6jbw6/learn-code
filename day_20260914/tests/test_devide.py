import sys
import os
# 导包失败 处理环境变量
# 当前环境变量应该在主目录下
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operation import devides
# import unittest

# class TestDevide(unittest.TestCase):
#     ''' 
#     测试 devide 函数
#     1. 测试 devide 函数的参数是否为整数
#     2. 测试 devide 函数的返回值是否为整数
#     3. 测试 devide 函数的返回值是否与预期结果一致
#     '''
#     def test_devide(self):
#         self.assertEqual(devides.devide(1, 1), 1)
#         self.assertEqual(devides.devide(10, 2), 5)
# # 调用
# if __name__ == '__main__':
#     unittest.main()

# pytest 测试devide模块 
def test_devide():
    assert devides.devide(1, 1) == ( 1)
