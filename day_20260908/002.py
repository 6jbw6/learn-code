class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # 初始里程数为0公里
        self.odometer = 0
        print(f"初始化方法被调用，{self.brand} {self.model} {self.year} 被创建了")
    
    def get_description(self):
        return f"{self.brand} {self.model} {self.year}，当前里程数为{self.odometer}公里"
    
    # 内部方法，用于修改里程数
    def update_odometer(self, mileage):
        # 禁止回调里程表 
        if mileage >= self.odometer:
            print("不能回调里程表")
        else:
            print("里程表不能回调")
    
my_new_car = Car("奔驰", "迈巴赫S级", 2026)
print(my_new_car.get_description())

# 3. 修改属性的值
my_new_car.odometer = 10000
print(my_new_car.get_description())

# 4. 调用内部方法
my_new_car.update_odometer(20000)
print(my_new_car.get_description())
