# l = [1, 2, 3, 4, 5]
#
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
#
# # for i in l:
# #     print(i)


# class MyRange:
#     def __iter__(self):
#         return self
#
#     def __init__(self, end):
#         self.i = -1
#         self.end = end
#
#     def __next__(self):
#         self.i += 1
#         if self.i < self.end:
#             return self.i
#         else:
#             raise StopIteration
#
#
# for i in MyRange(10):
#     print(i)


# class Fib:
#     def __iter__(self):
#         return self
#
#     def __init__(self, n):
#         self.i = -1
#         self.n = n
#
#         self.fib1 = 1
#         self.fib2 = 1
#
#     def __next__(self):
#         self.i += 1
#         if self.i < self.n:
#             self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
#             return self.fib2
#         else:
#             raise StopIteration
#
#
# for i in Fib(10):
#     print(i, end=' ')




def simple_generator(n):
    i = 0

    while i < n:
        yield i

        i += 1

i = simple_generator(3)
print(next(i))
print(next(i))
print(next(i))

print(next(i))



# for i in simple_generator(10):
#     print(i, end=' ')