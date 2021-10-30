def upper_attr(future_class_name, parents, future_class_attrs):
    print(future_class_attrs)
    upper_name_attrs = {}

    for name, val in future_class_attrs.items():
        if name.startswith('__'):
            upper_name_attrs[name] = val
        else:
            upper_name_attrs[name.upper()] = val

    return type(future_class_name, parents, upper_name_attrs)


class Foo(metaclass=upper_attr):
    bar = 'Hello'


print(hasattr(Foo, 'bar')) # False
print(hasattr(Foo, 'BAR')) # True

c = Foo()
print(c.BAR)

c.a = 5
print(c.a)
print(dir(c))