class MyClass:
    def __init__(self):
        self.var = 1

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        # object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('No attr')



c = MyClass()

print(c.dsf)