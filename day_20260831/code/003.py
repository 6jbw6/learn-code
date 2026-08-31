# 字符串 
# 字符串就是一系列的字符 string --> 关键字 str 
test_str_1 = "hel'l'o world"
test_str_2 = 'h"e"llo world'
test_str_3 = """
h'e'l"l"o world
"""
# 一 字符串的内置方法
# 1. 首字母大写
test_str_4 = ' hello world '
print(test_str_4.title())
# 2. 全大写
print(test_str_4.upper())
# 3. 全小写
print(test_str_4.lower())
# 4. 替换
# print(test_str_4.replace('l', '*'))
# 5. 查找 字符串 有序的--索引
print(test_str_4.find('l'))
print(test_str_4.index('l'))
# 6. 计算 字符串的长度
print(len(test_str_4))
# 7. 去空格
print(test_str_4.strip())
# 8. 切片
print(test_str_4[0:5])
print(test_str_4[0:5:2])
# 9. 换行、制表符、空格
test_str_6 = '春眠不觉晓\n鸟鸣声声\t月色满床'
print(test_str_6)
# 10. 字符串的拼接
print(test_str_1 + test_str_2)
print(test_str_3 + test_str_4)
# 11. 删除前缀
test_url = 'https://www.baidu.com'
print(test_url.removeprefix('https://'))

# 二 使用技巧 
# 1. 字符串可以当作序列操作 
test_str_7 = 'hello world'
for char in test_str_7:
    print(char)
# 2. 字符串的翻转
print(test_str_7[::-1])
print(''.join(reversed(test_str_7)))
# 3. 字符串的格式化操作 
stu_name = '张三'
stu_id = 1001
stu_age = 18
print(f'你好，{stu_name}，你的学号是:{stu_id}，你今年:{stu_age}岁了')
# 4. 判断字符串是否只包含数字
print('123'.isdigit())
print('123a'.isdigit())
# 5. 判断字符串是否只包含字母
print('abc'.isalpha())
print('abc123'.isalpha())
# 6. 规则表 替换
test_str_8 = '你好,你是新来的吗.'
# 创建规则表
# 1. 替换逗号和句号为中文逗号和中文句号
table = test_str_8.maketrans(',.', '，。')
print(test_str_8.translate(table))

#三 字符串与字节串
# 字符串：给人看的
# 字节串：给计算机看的
# 编码：将字符串转换为字节串
test_str_9 = 'hello world'
test_str_utf = test_str_9.encode('UTF-8')
print(test_str_utf)
# 解码：将字节串转换为字符串
print(test_str_utf.decode('UTF-8'))
