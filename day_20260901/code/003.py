# 三 字典 （dict）
# 1. 字典的概念
# 字典是一种无序的、可变的序列。字典中的元素是键值对，每个键值对之间用逗号隔开，每个键值对之间用冒号隔开。
# 字典的定义
test_dict_1 = {'name':'zhang san','age':18,'gender':'male'}
print(test_dict_1)
# 2. 访问字典中的元素
print(test_dict_1['name'])
print(test_dict_1['age'])
print(test_dict_1['gender'])
# 3. 字典的遍历
for key in test_dict_1:
    print(key)
    print(test_dict_1[key])

# 4. 字典的操作 
# get() 方法
get_testdict_age = test_dict_1.get('ages',0)
print(get_testdict_age)
# setdefault 方法取值并修改
# key 存在，不修改
# key 不存在，添加
test_dict_1.setdefault('ages',28)
print(test_dict_1)
# pop 方法删除指定的键值对
pop_result = test_dict_1.pop('ages',None)
print(pop_result)
print(test_dict_1)

# 5. 字典的推导式
test_dict_2 = {
    'foo':100,
    'bar':200,
}
test_dl = { key:value*2 for key,value in test_dict_2.items() if key == 'foo' }
print(test_dl)