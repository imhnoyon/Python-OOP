
import random
from school import School
class person:
    def __init__(self,name) -> None:
        self.name=name

class Teacher(person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1,100)
    

class Student(person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.marks={} # {"subject": 78,"subject" : 80}
        self.subject_grade = {} # {"subject" : 'A'}        
        self.grade = None #final grade


    def final_grade(self):
        sum=0
        for grade in self.final_grade.values():
            point = School.grade_to_value(grade)
            sum += point

        gpa=sum / len(self.subject_grade) # 7/2=3.5
        self.grade=School.value_to_grade(gpa)


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

