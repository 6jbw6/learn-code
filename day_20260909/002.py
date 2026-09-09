# 方式 1 
import ecommerce.payments
# 方式2 
from ecommerce import payments
# 方式3 
from ecommerce import *
# 方式4 
from ecommerce.payments import alipay_payment


# 信用卡支付逻辑
payments.credit_card_payment(100)
