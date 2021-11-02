from datetime import date


class Person:

    a = 10

    def __init__(self, name, age):
        print(f'self = {self}')
        self.name = name
        self.age = age

    @classmethod
    def from_birth_years(cls, name, year):
        print(f'cls = {cls}')
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person_1 = Person('Tom', 30)
person_2 = Person.from_birth_years('Anna', 2010)

print(id(Person.a))
print(id(person_1.a))
print(id(person_2.a))

print(Person.is_adult(20))
print(Person.is_adult(10))
