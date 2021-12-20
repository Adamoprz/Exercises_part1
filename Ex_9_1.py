class Student:
    def __init__(self, name: str, surname: str, index_id: int) -> None:
        self.name = name
        self.index_id = index_id
        self.surname = surname
    def describe_stud(self):
        print("Student {} {} ma nr indeksu {}".format(self.name, self.surname, self.index_id))

def main():
    student = Student("Marcin", "Kowalski" , 124)
    student.describe_stud()
    print(student.name)

if __name__ == "__main__":
    main()