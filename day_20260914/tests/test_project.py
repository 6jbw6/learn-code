import sys
import os
# 导包失败 处理环境变量
# 当前环境变量应该在主目录下
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operation import adds, devides
# 测试前后的操作 
import pytest
# import unittest

# class TestProject(unittest.TestCase):
#     '''
#     测试项目
#     1. 测试 add 函数
#     2. 测试 devide 函数
#     '''
#     def test_add(self):
#         self.assertEqual(adds.add(1, 1), 2)
#         self.assertEqual(adds.add(-1, 1), 0)
#         self.assertEqual(adds.add(0, 0), 0)
#         self.assertEqual(adds.add(-1, -1), -2)
#     def test_devide(self):
#         self.assertEqual(devides.devide(1, 1), 1)
#         self.assertEqual(devides.devide(10, 2), 5)
        
# if __name__ == '__main__':
#     unittest.main()
# 测试前后的操作 
@pytest.fixture
def db_obj():
    print('测试开始 连接数据库')
    test_str = '数据库对象'
    yield test_str
    print('测试结束 断开数据库')

# 加法测试
def test_add(db_obj):
    print(db_obj)
    assert adds.add(1, 1) == ( 2)

# 除法测试
def test_devide(db_obj):
    print(db_obj)
    assert devides.devide(1, 1) == ( 1)
    assert devides.devide(10, 2) == ( 5)
