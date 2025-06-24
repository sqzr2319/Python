#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/24 13:45
# @Author: ms169


class People:
    institution = "Tsinghua University"

    @classmethod
    def update_institution(cls, new_institution):
        cls.institution = new_institution

    @staticmethod
    def print_welcome():
        print("清华大学欢迎您！")

    def __init__(self, identity, name, email):
        self.identity = identity
        self.name = name
        self.email = email

    def update_identity(self, new_identity):
        self.identity = new_identity

    def update_name(self, new_name):
        self.name = new_name

    def update_email(self, new_email):
        self.email = new_email

    def print_info(self):
        print(f"ID: {self.identity}, Name: {self.name}, Email: {self.email}")


class Professor(People):
    def __init__(self, identity, name, email, level, courses, salary):
        super().__init__(identity, name, email)
        self.level = level
        self.courses = courses
        self.salary = salary

    def update_level(self, new_level):
        self.level = new_level

    def update_courses(self, new_courses):
        self.courses = new_courses

    def update_salary(self, new_salary):
        self.salary = new_salary

    def print_info(self):
        print(f"ID: {self.identity}, Name: {self.name}, Email: {self.email},"
              f"Level: {self.level}, Courses: {self.courses}, Salary: {self.salary}")


class Student(People):
    def __init__(self, identity, name, email, level, major, gpa):
        super().__init__(identity, name, email)
        self.level = level
        self.major = major
        self.gpa = gpa

    def update_major(self, new_major):
        self.major = new_major

    def update_level(self, new_level):
        self.level = new_level

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def print_info(self):
        print(f"ID: {self.identity}, Name: {self.name}, Email: {self.email},"
              f"Level: {self.level}, Major: {self.major}, GPA: {self.gpa}")


def main():
    # People 类使用示例
    People.print_welcome()

    p1 = People("P001", "Alice", "Alice001@tsinghua.edu.cn,")
    p1.print_info()

    People.update_institution("Peking University")
    p1.update_name("Alice Smith")
    p1.update_identity("P002")
    p1.update_email("Smith002@pku.edu.cn")

    p1.print_info()

    # Professor 类使用示例
    prof1 = Professor("Prof001", "Bob", "Bob001@mail.tsinghua.edu.cn",
                      "Associate Professor", ["CS101", "CS102"], 8000)
    prof1.print_info()

    prof1.update_salary(9000)
    prof1.update_courses(["CS101", "CS102", "CS103"])
    prof1.update_level("Vice Professor")
    prof1.update_email("114514@qq.com")

    prof1.print_info()

    # Student 类使用示例
    stu1 = Student("Stu001", "Charlie", "Charlie001@mails.tsinghua.edu.cn",
                   "Undergraduate", "Software Engineering", 3.8)
    stu1.print_info()

    stu1.update_major("Computer Science")
    stu1.update_gpa(3.9)
    stu1.update_level("Postgraduate")
    stu1.update_email("114514@qq.com")

    stu1.print_info()


if __name__ == "__main__":
    main()
