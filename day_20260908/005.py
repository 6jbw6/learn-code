# ocp 开闭原则
# 对扩展开放，对修改关闭
# 1. 新增功能时，只需要新增一个类/函数即可
# 2. 修改功能时，只需要修改一个类/函数即可
# 在不修改原有代码的情况下，实现新功能，避免引入新的错误，保证系统的稳定性

# 举例1：
class OtherPay:
    def __init__(self):
        pass

    def pay(self, pay_type):
        if pay_type == "al":
            print("支付宝支付")
        elif pay_type == "wechat":
            print("微信支付")
        elif pay_type == "bank":
            print("银行支付")
        elif pay_type == "cash":
            print("现金支付")
        else:
            print("其他支付方式")

# 利用abc模块编写 定义支付接口规则
from abc import ABC, abstractmethod

# 父类，定义支付接口规则
class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, pay_type):
        pass

# 微信支付类
class WechatPay(PaymentInterface):
    def pay(self, pay_type):
        print("微信支付")

# 支付宝支付类
class AlipayPay(PaymentInterface):
    def pay(self, pay_type):
        print("支付宝支付")

# 银行支付类
class BankPay(PaymentInterface):
    def pay(self, pay_type):
        print("银行支付")
