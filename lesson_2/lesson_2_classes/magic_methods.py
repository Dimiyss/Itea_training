class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f'STR: Name: {self.name}, age: {self.age}'
    #
    # def __repr__(self):
    #     return f'REPR: Name: {self.name}, age: {self.age}'

p = People('David', 20)

print(str(p))
print(repr(p))