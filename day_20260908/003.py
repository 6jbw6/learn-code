# 继承 
# 子类可以继承父类的属性和方法
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

# super() 特殊的函数，用于调用父类的初始化方法或方法
class SonCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        print(f"子类初始化方法被调用，{self.brand} {self.model} {self.year} 被创建了")
        self.battery_size = 60
    
    def describe_battery(self):
        print(f"{self.brand} {self.model} {self.year} 有 {self.battery_size} kWh 电池")

my_new_car = SonCar("特斯拉", "modely", 2026)
my_new_car.describe_battery()
