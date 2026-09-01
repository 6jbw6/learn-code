# 条件分支 （流程控制）
# 1. 语法结构 
# 条件分支的语法结构如下：
# if 条件:
#     代码块
# else:
#     代码块
USERNAME = 'root'
PASSWORD = '123456'
STATUS = 'active'
CODE = '1234567890'
if USERNAME == 'root':
    if PASSWORD == '123456':
        print('登录成功')
        if CODE == '1234567890':
            print('验证码正确')
            if STATUS == 'active':
                print('用户状态正常')
            else:
                print('用户状态异常')
        else:
            print('验证码错误')
    else:
        print('密码错误')
else:
    print('用户名错误')

#2. 分支的基础
# 单项分支
test_str = 'aaa'
if test_str.isalpha():
    print('字符串只包含字母')
# 双项分支
if test_str.isalpha():
    print('字符串只包含字母')
else:
    print('字符串包含其他字符')
# 多项分支
if test_str.isalpha():
    print('字符串只包含字母')
elif test_str.isdigit():
    print('字符串只包含数字')
else:
    print('字符串包含其他字符')
# 判断
# if test_str.isalpha() == True:
#     print('字符串只包含字母')
if test_str.isalpha():
    print('字符串包含其他字符')
# 各个数据类型 为False的情况
# 空列表 []
# 空字符串 ''
# 空元组 ()
# 空字典 {}
# 空集合 set()
# None
# bool 为 False
# 空整数 0
# 空浮点数 0.0
# 空复数复数 0.0j
if not test_str:
    print('字符串为空')

# 3. 三元表达式
test_str = 'aaa'
result = '字符串只包含字母' if test_str.isalpha() else '字符串包含其他字符'
print(result)



    