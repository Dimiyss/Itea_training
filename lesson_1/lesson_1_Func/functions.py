# def add(*qwe):
#     sum = 0
#     for i in qwe:
#         sum += i
#     return sum
#
#
# def test_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
#
# # print(add(1, 2, 3, 4, 5, 6))
# test_func(a=1, b=2)



# def func(a, b):
#     return a+1, b-2
#
# def func_2(a, b, c):
#     return a+b+c
#
# print( func_2( *func(1, 5), 5 ) )
#
#
# print(*func(1, 5))


a = 5
b = 6



# print(f'a = {a}')
# print(f'b = {b}')
#
# a, b = b, a
#
# print(f'a = {a}')
# print(f'b = {b}')


# print('a =' + str(a))
# print('a = %d\nb = %d' % (a, b))
# print('a = {0}\nb = {1}\na = {0}'.format(a, b))

from random import randint

for i in range(10):
    for j in range(10):
        print(f'{randint(0, 99999):^7}', end='')
    print()

