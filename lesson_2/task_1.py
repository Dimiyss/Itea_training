class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_mark(self):
        return sum(self.marks) / len(self.marks)



student_1 = Student('Nik', [1, 2, 3, 3, 1])
student_2 = Student('Nik2', [1, 1, 3, 3, 1])
student_3 = Student('Nik3', [4, 2, 3, 3, 1])
student_4 = Student('Nik4', [2, 2, 3, 3, 1])
student_5 = Student('Nik5', [3, 2, 3, 3, 1])

lst_st = [student_1, student_2, student_3, student_4, student_5]

def print_sorted(students):
    for student in sorted(students, key=lambda x: x.avg_mark(), reverse=True):
        print(f'Name {student.name}, {student.avg_mark()}')

print_sorted(lst_st)