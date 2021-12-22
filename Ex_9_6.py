import datetime
import time

class Note:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.date = datetime.datetime.now()
    def return_exist_note(n1):
        return n1
    def return_note(self):
         return [self.author, self.text, self.date]

class Notebook:
    def __init__(self):
        self.list_of_notes = []
    def add_note(self, author, text):
        new_note = Note(author, text)
        self.list_of_notes.append(new_note.return_note())
    def add_exist_note(self, n1):
        temp_note = n1.return_note()
        self.list_of_notes.append(temp_note)
    def count_notes(self):
        print(len(self.list_of_notes))
    def show_notes(self):
        print("Masz takie notatki: ")
        count = 0
        for note in self.list_of_notes:
            count += 1
            print(f'{count}.  {note[0]}: "{note[1]}" o godzinie {note[2].hour}:{note[2].minute}')

def main():

    nb = Notebook()
    nb.add_note("Bartek", "Dokonczyc instrukcje")
    nb.show_notes()
    # test time skip note
    time.sleep(61)
    n1 = Note("Andrii", "Sprawdzic instrukcje ")
    # test time skip note
    time.sleep(61)
    nb.add_exist_note(n1)
    nb.show_notes()


if __name__ == "__main__":
    main()