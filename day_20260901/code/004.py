# 四 集合 （set）
# 1. 集合的概念
# 集合是一种无序的、不可重复的序列。集合中的元素是唯一的，不能重复。
# 集合的定义
test_set_1 = {10, 20, 30, 40, 50}
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
