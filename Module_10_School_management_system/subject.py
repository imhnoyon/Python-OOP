from school import Student
from person import School

class Subject:
    def __init__(self,name,teacher) -> None:
        self.name=name
        self.teacher=teacher
        self.Max_marks=100
        self.pass_marks=33

    def exam(self,students):
        for student in students:
            mark=self.teacher.evaluate_exam()
            Student.marks[self.name]=mark
            Student.subject_grade[self.name]=School.calculate(mark)

        