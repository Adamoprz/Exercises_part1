class Student:
    #def __init__(self, name : str, index_id : int) -> None:
    def __init__(self, name, surname, index_id):
        self.name = name
        self.index_id = index_id
        self.surname = surname
    def __str__(self):
        return "Student {} {} ma nr indeksu {}".format(self.name, self.surname, self.index_id)
#
student = Student("Marin", "Kowalski" , 124)
print(student)