#1.  变量的声明
#  变量：用于存储数据的容器
#  数据类型：变量可以存储的数据类型

name = '张三'
age = 18
# 2. 变量的命名规则与注意事项
#  变量名：由字母、数字、下划线组成，不能以数字开头
#  注意事项：不能使用Python保留字，不能使用特殊字符，不能使用空格
student_name = '张三'
s_n = '张三'
# 3. 变量的常见方法
author = '张三'

# 操作多个变量 
name,age = '张三',18

# 变量的解包
usernames = ['张三','李四','王五']
zhangsan,lisi,wangwu = usernames
attrs = [1,["张三","李四","王五"]]
user_id,(name1,name2,name3) = attrs
data = [1,2,3,4,5,6]
# 动态解包
username,*other,age = data

# 4. 变量声明（注意事项）
# 单下划线--约定俗成
usernames = ['张三','无名氏']
author,_ = usernames
#
data1 = 111
data2 = 9888
if data1 == data2:
    print('相等')
# PEP8 原则
# 普通变量使用蛇形命名法
# data_userid = 111
# data_systemid = 888
# 常量采用全部大写的方法
MODEL_PATH = 'model.pth'
DATASET_PATH = 'TEST.csv'
# 仅内部使用变量
_local_var = 100
# 当名字与python关键字冲突时，在变量末尾使用下划线
class_ = 'class_name'
# 驼峰风格
userName = '张三'
UserWarning = '警告信息'

# 增强描述性
s = ' hello world '
def test(strs):
    print(strs)
# 弱描述性
value = test(s.strip()) 
# 强描述性
input_str = 'hello world'
username = test(input_str.strip())
# 尽量要短
stu_name = 'hello world'
username = test(stu_name.strip())

# 5. 变量声明匹配数据类型
# is_superuser	 是否是超级管理员	是/不是
# has_error	     有没有错误	         有/没有
# allow_empty	 是否允许空值	    允许/不允许
# user_id	     用户id	数值
# doubao_port	 大模型服务端口	     数值
# max_length	 最大长度	
# phone_price_max	最大价格	    数值

# 6. 变量命名简便方法
# 数组命名 i，j,k
# 某个整数 n
# 某个字符串 s
# 某个异常 e
# 文件对象 fp
