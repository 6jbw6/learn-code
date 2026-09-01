# 四 集合 （set）
# 1. 集合的概念
# 集合是一种无序的、不可重复的序列。集合中的元素是唯一的，不能重复。
# 集合的定义
test_set_1 = { 10, 20, 30, 40, 50 }
print(test_set_1)

# 定义一个空集合
empty_set = set()
print(empty_set)

# 2. 集合的遍历
for item in test_set_1:
    print(item)

# 3. 集合的推导式
test_set_3 = {1,2,3,4,5,6}
test_set_3_result = { i for i in test_set_3 if i % 2 == 0 }
print(test_set_3_result)

# 4. 集合的操作 
# 追加元素
test_set_3.add(60)
print(test_set_3)

# 5. 冰冻集合
# 冰冻集合是一种不可变的集合，一旦创建，就不能修改。
# 冰冻集合的定义
frozen_set_1 = frozenset(test_set_3)
print(frozen_set_1)

# 6. 集合的运算 
# 并集
union_result = test_set_1 | test_set_3
print(union_result)
# 交集
intersection_result = test_set_1 & test_set_3
print(intersection_result)
# 差集
difference_result = test_set_1 - test_set_3     
print(difference_result)
# 对差差集
symmetric_difference_result = test_set_1 ^ test_set_3
print(symmetric_difference_result)
# 子集
issubset_result = test_set_1.issubset(test_set_3)
print(issubset_result)
# 超集
issuperset_result = test_set_1.issuperset(test_set_3)
print(issuperset_result)