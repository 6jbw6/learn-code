# 文件读取 功能 
# author: zhang san 
# date: 2026-09-02
# version: 1.0
# description: 读取data.txt文件，打印文件内容
import os 
# 设置环境变量
os.environ['TRAIN_DATA_FILE'] = 'data.txt'

# 读取环境变量中的路径变量
TRAIN_DATA_FILE = 'data.txt'

# 环境变量处理
# 如果环境变量不统一，可能会出现路径错误
try:
    # 打开了一个文件对象
    with open(TRAIN_DATA_FILE, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print("异常：", e)
# 返回结果
else:
    print("文件存在")
    print(content)
# 无论是否发生异常，都执行的代码块
finally:
    # 关闭文件对象
    f.close()
