from time import sleep, time


def benchmark(method):
    def helper(*args, **kwargs):
        time_start = time()
        res = method(*args, **kwargs)
        print(f'Time process: {time() - time_start} sec.')
        return res

    return helper

def decor_benchmakr_methods(cls):
    # class NewClass:
    #     def __init__(self, *args, **kwargs):
    #         self._obj = cls(*args, **kwargs)
    #
    #     def __getattribute__(self, item):
    #         try:
    #             is_my_attr = super(NewClass, self).__getattribute__(item)
    #         except AttributeError:
    #             pass
    #         else:
    #             return is_my_attr
    #
    #         attr = self._obj.__getattribute__(item)
    #
    #         if callable(attr):
    #             return benchmark(attr)
    #         else:
    #             return attr
    # return NewClass

    def helper(*args, **kwargs):
        for attr in dir(cls):
            if attr.startswith('__'):
                continue

            new_attr = getattr(cls, attr)

            if callable(new_attr):
                decor_method = benchmark(new_attr)
                setattr(cls, attr, decor_method)
        return cls(*args, **kwargs)
    return helper

@decor_benchmakr_methods

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method_1(self, n):
        print(f'[{time()}] Starting method #1')
        sleep(n)
        print(f'[{time()}] Finished method #1')


t = Test(5, 6)
t.method_1(1)