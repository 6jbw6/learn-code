import sys
import os
# 导包失败 处理环境变量
# 当前环境变量应该在主目录下
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operation import adds

# pytest 测试add模块 
def test_add():
    assert adds.add(1, 1) == ( 2)