# 容器数据类型
# 一 列表 （list）
# 1. 列表的概念
# 列表是由一系列特定顺序排列的元素组成的。字母、数字、字符串、元组、字典、集合等，组成多维列表。
# 列表的定义
test_list_1 = [10, 20, 30, 40, 50,'a','zhang san',[1,2,3,[3,4,5]]]
print(test_list_1)

# 2. 访问列表中的元素
# 索引<-->获取列表中的元素
print(test_list_1[0]) 
print(test_list_1[6].title())
print(test_list_1[7][0])
print(test_list_1[7][1])
print(test_list_1[7][2])
print(test_list_1[7][3][0])
# 切片
print(test_list_1[0:5:2])
print(test_list_1[5:])
print(test_list_1[:5])

# 3. 列表中元素的修改、添加、删除
test_list_2 = ['a','b','c','d','e']   
test_list_2[0] = 'A'
print(test_list_2)
# 追加 
test_list_2.append('F')
print(test_list_2)
# 插入
test_list_2.insert(2,'C')
print(test_list_2)
# 删除 
del test_list_2[2]
print(test_list_2)
# pop
print(test_list_2)
pop_result = test_list_2.pop()
print(pop_result)
print(test_list_2)
# pop 删除任意位置元素
pop_result = test_list_2.pop(2)
print(pop_result)
print(test_list_2)
# 删除指定的元素 remove(删除元素)
# 删除第一个匹配的元素
test_list_3 = ['a','b','c','c','c','d','e']
test_list_3.remove('c')
print(test_list_3)

# 4. 管理列表
# 排序 
test_list_4 = [10, 20, 30, 40, 50]
test_list_4.sort()
print(test_list_4)
# 反转排序
test_list_4.sort(reverse=True)
print(test_list_4)
test_list_5 = ['zhang san','liisi','wangwu','zhaoliu']
# test_list_5.sort()
print(test_list_5)
# 临时排序
print(sorted(test_list_5))
print(test_list_5)
# 反序
test_list_5.reverse()
print(test_list_5)

# 5. 确定列表的长度
print(len(test_list_5))

# 6. 列表的遍历
for item in test_list_5:
    print(item)

# 7. 创建数值列表 
for i in range(10):
    print(i)
for i in range(1,9,2):
    print(i)
# 从大到小 反序
for i in range(9,0,-1):
    print(i)
# 数值列表简单的统计计算
print(sum(test_list_4))
print(max(test_list_4))
print(min(test_list_4))

# 8. 列表推导式 
test_list_6 = [ i for i in range(10) ]
# 带有分支的列表推导式
test_list_7 = [ i**2 for i in range(10) if i % 2 == 0 ]
print(test_list_7)
