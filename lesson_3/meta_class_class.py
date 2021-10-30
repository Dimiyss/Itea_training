class UpperAttr(type, ):
    def __new__(cls, future_class_name,
                future_class_parents, future_class_attrs):

        upper_name_attrs = {}

        for name, val in future_class_attrs.items():
            if name.startswith('__'):
                upper_name_attrs[name] = val
            else:
                upper_name_attrs[name.upper()] = val

        # return type.__new__(cls, future_class_name, future_class_parents, upper_name_attrs)
        return super().__new__(cls, future_class_name, future_class_parents, upper_name_attrs)

class Foo(metaclass=UpperAttr):
    bar = 'Hello'


print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True
