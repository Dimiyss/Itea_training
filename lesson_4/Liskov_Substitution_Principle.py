# def AnimalLegCount(animals):
#     for animal in animals:
#         if type(animal) is Lion:
#             return LionLegCount(animal)
#         if type(animal) is Mouse:
#             return MouseLegCount(animal)
#         if type(animal) is Snake:
#             return SnakeLegCount(animal)


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getLegCount(self):
        pass


class Lion(Animal):
    def getLegCount(self):
        return 4


class Mouse(Animal):
    def getLegCount(self):
        return 4


class Snake(Animal):
    def getLegCount(self):
        return 0


def AnimalLegCount(animals):
    for animal in animals:
        print(animal.getLegCount())


animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
]

AnimalLegCount(animals)
