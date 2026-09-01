#  二 元组 （tuple）
# 1. 元组的概念
# 元组是一种有序的、不可变的序列。元组中的元素可以是任意数据类型，包括数字、字符串、列表等。
# 元组的定义
test_tuple_1 = (10, 20, 30, 40, 50)
print(test_tuple_1)

# 2. 访问元组中的元素
print(test_tuple_1[0])
# 切片
print(test_tuple_1[0:5:2])
print(test_tuple_1[5:])
print(test_tuple_1[:5])

# 3. 元组的遍历
for item in test_tuple_1:
    print(item)