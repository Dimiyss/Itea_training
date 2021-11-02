from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say(self):
        print('Say: ', end='')


class Cat(Animal):
    def say(self):
        super(Cat, self).say()
        print('Mya-mya')

# Error
# animal_1 = Animal('Rock')


cat_1 = Cat('Rock')
cat_1.say()


# For TESR
# for install: pip install python-interface
# from interface import implements, Interface
#
# class MyInterface(Interface):
#
#     def method1(self, x):
#         pass
#
#     def method2(self, x, y):
#         pass