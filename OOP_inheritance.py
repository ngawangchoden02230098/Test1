class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def common_behavior(self, walk, talk, eat, sleep):
        self.walk = walk
        self.talk = talk
        self.eat = eat
        self.sleep = sleep


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teacher_behavior(self, teach, grade_students, attend_meeting):
        self.teach = teach
        self.grade_students = grade_students
        self.attend_meeting = attend_meeting


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa


obj1 = Student("Tshewang", 21, 11506008012, 2230115, "ECE", "1st Year", 70)
print(f"The student {obj1.name} is {obj1.age} years old bearing CID number {obj1.cid_number}. His Student ID is {obj1.student_id} and he is studying {obj1.course} in {obj1.year}. His aggregate is {obj1.gpa}.")
