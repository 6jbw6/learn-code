import sys
import os
# 导包失败 处理环境变量
# 当前环境变量应该在主目录下
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operation import adds
import unittest



class TestAdd(unittest.TestCase):
    '''
    测试 add 函数
    1. 测试 add 函数的参数是否为整数
    2. 测试 add 函数的返回值是否为整数
    3. 测试 add 函数的返回值是否与预期结果一致
    '''
    def test_add(self):
        self.assertEqual(adds.add(1, 1), 2)
        self.assertEqual(adds.add(-1, 1), 0)
        self.assertEqual(adds.add(0, 0), 0)
        self.assertEqual(adds.add(-1, -1), -2)


# 调用
if __name__ == '__main__':
    unittest.main()
