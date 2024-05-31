#multiple inheritance

class Family:
    def __init__(self,father,Mother) -> None:
        self.father=father
        self.Mother=Mother

class school:
    def __init__(self,Name,id) -> None:
        self.Name=Name
        self.id = id

class student(Family,school):
    def __init__(self, father, Mother,Name,id) -> None:
         school.__init__(self,Name,id)
         Family.__init__(self,father,Mother)