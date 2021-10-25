# print(1 + 1)
# print('1' + '1')

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_full_info(self):
        print(f'Name: {self.name}, age: {self.age}')

    def say(self):
        raise Exception('Must overrided')

class Dog(Animal):
    def say(self):
        print('Woof, woof!')

class Cat(Animal):
    def say(self):
        print('Mya, Mya!')


dog_1 = Dog('Bim', 5)
# dog_1.print_full_info()
# dog_1.say()

cat_1 = Cat('Rock', 3)
# cat_1.print_full_info()
# cat_1.say()

animals = [cat_1, dog_1, Cat('Zen', 15)]

for animal in animals:
    animal.say()