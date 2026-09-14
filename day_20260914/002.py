import pytest

# python 安装第三方模块
# 1.  可以使用 pip 安装
# 临时更换安装源
# pip install 模块名 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装pytest
# pip install pytest -i https://pypi.tuna.tsinghua.edu.cn/simple
# 2. conda 安装
# conda install 模块名 -c base -n conda-forge
# 3. uv 安装
# uv add 模块名

# pytest的使用方法
# @pytest.fixture()
# 函数级别
# @pytest.fixture(scope='function')  # 每个测试函数执行前执行
# 类级别
# @pytest.fixture(scope='class')  # 每个测试类执行前执行
# 模块级别
# @pytest.fixture(scope='module')  # 每个测试模块执行前执行
# 系统级别
# @pytest.fixture(scope='session')  # 每个测试会话执行前执行
# 例如 数据库连接这种操作，可以设置成session级别，所有的测试只连接一次
@pytest.fixture(scope='session')
def db_obj():
    print('测试开始 连接数据库')
    test_str = '数据库对象'
    yield test_str
    print('测试结束 断开数据库')

# 测试数据库添加用户
def test_add_user(db_obj):
    # 测试添加用户
    db_obj.execute('insert into user (name, password) values ("张三", "123456")')
    # 测试查询用户
    result = db_obj.execute('select password from user where name = "张三"').fetchone()[0]
    # 测试查询结果是否正确
    assert result == '张三'
