class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade

    def get_grade(self):
        return self.grade

class Classroom:
    def __init__(self):
        self.students=[]

    def add_students(self,student):
        self.students.append(student)

    def remove_students(self,student):
        self.students.append(student)

    def average_score(self):
        students=self.students
        avg_grade=0
        for j in students:
            avg_grade+=j.get_grade()
        avg_grade/=len(students)
        return avg_grade