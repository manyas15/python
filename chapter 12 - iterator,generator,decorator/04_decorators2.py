# @staticmethod
# A static method is a method that belongs to a class but does not need access to the class or object.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))

# @staticmethod tells Python that this method doesn't need self or cls.
# We can call it directly using the class name.


# @classmethod
# A class method works with the class itself rather than a particular object.
# It uses cls as its first parameter.

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()


# @property
# This decorator allows us to access a method like an attribute, without using parentheses.

class Student:

    def __init__(self, name):
        self.name = name

    @property
    def student_name(self):
        return self.name


s = Student("Manya")

print(s.student_name)

# Normally, we call a method like this:
# s.student_name()

# But with @property, we write:
# s.student_name
# It looks like accessing a variable!