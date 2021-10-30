# Decorator
########################################################################################################################
def decor(cls):
    cls.func_1 = lambda self: print('Hello World')
    return cls


@decor
class Cls_1:
    pass


class Child_Cls_1(Cls_1):
    def func_1(self):
        print('Hello')


obj = Child_Cls_1()
obj.func_1()



# Meta-class
########################################################################################################################
class Meta(type):
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls.func_1 = lambda self: print('Hello World')

class Cls_2(metaclass=Meta):
    pass


class Child_Cls_2(Cls_2):
    def func_1(self):
        print('Hello')


obj2 = Child_Cls_2()
obj2.func_1()



