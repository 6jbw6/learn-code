# ISP 接口隔离原则
# 对于一个类，它实现的接口应该是它需要的，而不是它不需要的接口
# 不要把多个方法放到一个接口中，每个方法都有自己的职责
# 核心思想：小而专，不要大而全
# 避免接口污染、减少无用代码、降低耦合度、提高内聚性

# 举例1
from abc import ABC, abstractmethod

class MultiFunctionDevice(ABC):
    # 扚印文档
    @abstractmethod
    def print_document(self,data):
        pass
    # 扫描文档
    @abstractmethod
    def scan_document(self):
        pass
    # 发送文档
    @abstractmethod
    def fax_document(self,data):
        pass

    # 复印文档
    @abstractmethod
    def copy_document(self,data):
        pass

# 设备1 老打印机，只能打印 
class OldPrinter(MultiFunctionDevice):

    def print_document(self,data):
        print(f"打印：{data}")

    def scan_document(self):
        # 主动抛出异常
        raise NotImplementedError("老打印机不能扫描文档")

    def fax_document(self,data):
        # 主动抛出异常
        raise NotImplementedError("老打印机不能发送文档")

    def copy_document(self,data):
        raise NotImplementedError("老打印机不能复制文档")   

# 使用场景
# 1. 接口方法过多，类只需要实现其中的一部分方法
# 例如：打印机接口，老打印机只需要实现打印方法，不需要实现扫描、发送、复制方法
# 2. 实现类被迫写空方法或抛出异常，导致代码冗余
# 例如：打印机接口，老打印机不需要实现扫描、发送、复制方法，但是老打印机类中必须实现这3个方法，导致代码冗余
# 3. 修改一个接口，会导致所有实现类都必须修改，导致代码量增加
# 例如：打印机接口，新增一个复制文档方法，所有实现类都必须实现这个方法，导致代码量增加

# 举例2
# 打印机接口
class PrinterInterface(ABC):
    @abstractmethod
    def print_document(self,data):
        pass

# 扫描仪
class ScannerInterface(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# 传真机
class FaxInterface(ABC):
    @abstractmethod
    def fax_document(self,data):
        pass

class OldPrinter(PrinterInterface):
    def print_document(self,data):
        print(f"打印：{data}")

class NewPrinter(PrinterInterface, ScannerInterface, FaxInterface):
    def print_document(self,data):
        print(f"打印：{data}")
    def scan_document(self):
        print("扫描文档")
    def fax_document(self,data):
        print("发送文档")

# 只需要打印文档的使用场景
def print_document(printer,data):
    printer.print_document(data)

# 使用场景
print_document(OldPrinter(),"老打印机")
print_document(NewPrinter(),"新型打印机")





