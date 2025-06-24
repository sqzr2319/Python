#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/24 15:44
# @Author: ms169
import testPackage.calculate as calc
from testPackage.people import People
from testPackage.people import Professor as Prof


def main():
    # 使用 People 类
    People.print_welcome()
    person = People("001", "张三", "zs001@gmail.com")
    person.print_info()

    # 使用 Professor 类
    prof = Prof("002", "李四", "ls002@gmail.com", "Professor", ["CS101", "CS102"], 8000)
    prof.print_info()

    # 使用 calculate 模块
    area = calc.Striangle(3, 4, 5)
    print(f"三角形面积: {area}")


if __name__ == "__main__":
    main()
