class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Name: {self.name}, avg mark: {sum(self.marks) / len(self.marks)}'

    def __lt__(self, other):
        return sum(self.marks) / len(self.marks) < sum(other.marks) / len(other.marks)


def print_sorted_marks(students):
    # for student in sorted(students, reverse=True):
    for student in sorted(students, key=lambda x: sum(x.marks) / len(x.marks), reverse=True):
        print(student)


students = [
    Student('Ivan', [1, 1, 1, 1, 1]),
    Student('Petr', [2, 2, 2, 2, 2]),
    Student('Anna', [3, 3, 3, 3, 3]),
    Student('Lisa', [4, 4, 4, 4, 4]),
    Student('Den', [5, 5, 5, 5, 5]),
]
print_sorted_marks(students)

# print(5 < 6)
# print( Student('Ivan', [1, 1, 1, 1, 1]) < Student('Petr', [2, 2, 2, 2, 2]))