# def func_decor_args(n):
#     def func_decor(func):
#         def helper():
#             for i in range(n):
#                 func()
#         return helper
#     return func_decor


class Decorator:
    def __init__(self, n):
        self.n = n

    def test_func(self):
        print('this is test')

    def __call__(self, func):
        def helper():
            self.test_func()
            for i in range(self.n):
                func()
        return helper

@Decorator(3)
def foo():
    print('Hello')

foo()