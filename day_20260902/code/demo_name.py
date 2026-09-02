"""
学生点名器程序
功能：添加学生、删除学生、随机抽取学生、查看所有学生
作者：zhang san
日期：2026-09-02
"""
import random


class StudentNamer:

    def __init__(self):
        self._students = []
    def add_student(self, name: str) -> bool:
        """
        添加学生到名单
        """
        # 去除首尾空白
        name = name.strip()
        # 验证姓名非空
        if not name:
            raise ValueError("学生姓名不能为空！")

        # 检查是否已存在
        if name in self._students:
            raise ValueError(f"学生 '{name}' 已存在！")

        # 添加到列表
        self._students.append(name)
        return True

    def remove_student(self, name: str) -> bool:
        """
        从名单中删除学生

        Args:
            name: 学生姓名

        Returns:
            bool: 删除成功返回True

        Raises:
            ValueError: 学生不存在时抛出
        """
        name = name.strip()

        if not name:
            raise ValueError("学生姓名不能为空！")

        if name not in self._students:
            raise ValueError(f"学生 '{name}' 不存在！")

        self._students.remove(name)
        return True

    def random_pick(self, count: int = 1) -> list:
        """
        随机抽取指定数量的学生

        Args:
            count: 抽取人数，默认为1

        Returns:
            list: 被抽中的学生名单

        Raises:
            ValueError: 参数不合法时抛出
        """
        # 验证学生列表非空
        if not self._students:
            raise ValueError("学生名单为空，无法抽取！")

        # 验证抽取数量
        if count <= 0:
            raise ValueError("抽取数量必须大于0！")

        # 抽取数量不能超过学生总数
        if count > len(self._students):
            raise ValueError(
                f"抽取数量({count})不能超过学生总数({len(self._students)})！"
            )

        # 使用 random.sample 进行不重复随机抽取
        return random.sample(self._students, count)

    def show_all(self) -> list:
        """
        获取所有学生名单

        Returns:
            list: 学生名单副本
        """
        return self._students.copy()

    def get_count(self) -> int:
        """
        获取学生总数

        Returns:
            int: 学生数量
        """
        return len(self._students)

    def clear(self) -> None:
        """清空所有学生"""
        self._students.clear()


def print_menu():
    """打印主菜单"""
    print("\n" + "=" * 40)
    print("           学生点名器")
    print("=" * 40)
    print("  1. 添加学生")
    print("  2. 删除学生")
    print("  3. 随机抽取学生")
    print("  4. 查看所有学生")
    print("  5. 清空所有学生")
    print("  0. 退出程序")
    print("=" * 40)


def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    获取整数输入，带验证

    Args:
        prompt: 输入提示
        min_val: 最小值限制
        max_val: 最大值限制

    Returns:
        int: 有效的整数值
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"⚠️  输入必须大于等于 {min_val}！")
                continue
            if max_val is not None and value > max_val:
                print(f"⚠️  输入必须小于等于 {max_val}！")
                continue
            return value
        except ValueError:
            print("⚠️  请输入有效的数字！")


def main():
    """主函数 - 程序入口"""
    namer = StudentNamer()

    print("\n📚 欢迎使用学生点名器！")

    while True:
        print_menu()
        choice = get_int_input("请输入选项 (0-5): ", 0, 5)

        # 选项 1: 添加学生
        if choice == 1:
            print("\n--- 添加学生 ---")
            name = input("请输入学生姓名（输入 'q' 返回）: ").strip()

            if name.lower() == 'q':
                continue

            try:
                namer.add_student(name)
                print(f"✅ 学生 '{name}' 添加成功！")
                print(f"📊 当前学生总数: {namer.get_count()} 人")
            except ValueError as e:
                print(f"❌ 添加失败: {e}")

        # 选项 2: 删除学生
        elif choice == 2:
            print("\n--- 删除学生 ---")

            if namer.get_count() == 0:
                print("⚠️ 学生名单为空，无法删除！")
                continue

            # 显示所有学生供选择
            students = namer.show_all()
            print("当前学生列表:")
            for i, name in enumerate(students, 1):
                print(f"  {i}. {name}")

            name = input("\n请输入要删除的学生姓名（输入 'q' 返回）: ").strip()

            if name.lower() == 'q':
                continue

            try:
                namer.remove_student(name)
                print(f"✅ 学生 '{name}' 删除成功！")
                print(f"📊 当前学生总数: {namer.get_count()} 人")
            except ValueError as e:
                print(f"❌ 删除失败: {e}")

        # 选项 3: 随机抽取学生
        elif choice == 3:
            print("\n--- 随机抽取学生 ---")

            if namer.get_count() == 0:
                print("⚠️ 学生名单为空，无法抽取！")
                continue

            print(f"📊 当前学生总数: {namer.get_count()} 人")

            count = get_int_input(
                f"请输入要抽取的人数 (1-{namer.get_count()}): ",
                1,
                namer.get_count()
            )

            try:
                picked = namer.random_pick(count)
                print("\n" + "=" * 30)
                print("🎉 抽取结果:")
                print("=" * 30)
                for i, name in enumerate(picked, 1):
                    print(f"  第 {i} 名: {name}")
                print("=" * 30)
            except ValueError as e:
                print(f"❌ 抽取失败: {e}")

        # 选项 4: 查看所有学生
        elif choice == 4:
            print("\n--- 查看所有学生 ---")

            students = namer.show_all()
            count = namer.get_count()

            print("=" * 30)
            if count == 0:
                print("📭 学生名单为空")
            else:
                print(f"📋 学生名单 (共 {count} 人):")
                print("-" * 30)
                for i, name in enumerate(students, 1):
                    print(f"  {i:3d}. {name}")
            print("=" * 30)

        # 选项 5: 清空所有学生
        elif choice == 5:
            print("\n--- 清空所有学生 ---")

            if namer.get_count() == 0:
                print("⚠️ 学生名单已经为空！")
                continue

            confirm = input(
                f"⚠️  确定要清空所有 {namer.get_count()} 名学生吗？(y/n): "
            ).strip().lower()

            if confirm == 'y':
                namer.clear()
                print("✅ 已清空所有学生！")
            else:
                print("❎ 已取消清空操作")

        # 选项 0: 退出程序
        elif choice == 0:
            print("\n👋 感谢使用学生点名器，再见！")
            break


if __name__ == "__main__":
    main()
