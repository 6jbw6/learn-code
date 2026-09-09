# 物流模块
# 称重
def weight_check(weight):
    if weight > 100:
        print("重量超过限制")
    else:
        print("重量正常")

# 计算运费
def calculate_shipping(weight, distance):
    return weight * distance * 0.05
