# def greet(greeting, name):
#     print(greeting + ', ' + name)

def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)
    return greet

greet_hello = greet_curried('Hello')


greet_hello('German')
greet_hello('Ivan')

greet_curried('Hi')('Anna')




#
# # или напрямую greet_curried
# greet_curried('Hi')('Roma')
#
#
# greet('Hello', 'German')
# # ...
# greet('Hello', 'Ivan')
# # ...
# greet('Hello', 'Petr')
# # ...
# greet('Hello', 'Anna')