
MyClass = type('MyClass', (), {})

c = MyClass()

print(type(c))
print(dir(c))


class Foo:
    bar = 1

Foo_Type = type('Foo_Type', (), {'bar': 1, 'printBar': lambda self: print('bar') })

c1 = Foo()
print(c1.bar)

c2 = Foo_Type()
print(c2.bar)

c2.printBar()

print(hasattr(Foo_Type, 'bar2'))
Foo_Type.bar2 = 2
print(hasattr(Foo_Type, 'bar2'))

print(c2.bar2)