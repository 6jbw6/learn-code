# 使用 python 开发大型项目
# 1. 测试
#   a. UI测试
#   b. 集成测试
#   c. 单元测试
# unittest 框架
# 2. 使用方法
#   a. 导入 unittest 模块
#   b. 继承 unittest.TestCase 类
#   c. 定义测试方法
#       c1. 测试方法名必须以 test_ 开头
#       c2. assertEqual 方法用于断言两个值是否相等
#       c3. assertNotEqual 方法用于断言两个值是否不相等
#       c4. assertIsNone 方法用于断言一个值是否为 None
#       c5. assertIsNotNone 方法用于断言一个值是否不为 None
#   d. 断言测试结果
import unittest


# 继承了 unittest.TestCase 类
class TestStringUpper(unittest.TestCase):

    # 测试字符串的 upper 方法是否正常工作
    def test_upper(self):
        # 断言 'foo'.upper() 等于 'FOO' ，否则抛出异常
        self.assertEqual('foo1'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()