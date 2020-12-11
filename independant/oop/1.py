# objects can be of class int, string (etc) as well as function

# object type = __main__.Dog
class Dog:
    # Special method - called when new object is instantitated
    def __init__(self, name):
        self.name = name

    def bork(self):
        return "Bork"

    def bark(self):
        print("Bark")


d = Dog("Woofles")

# print(d.name)
# d.bark()
# print(d.bork())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        pass


s = Student("Ben", 18, 95)
course = Course("CompSci", 10)
course.add_student(s)

print(course.students[0].name)