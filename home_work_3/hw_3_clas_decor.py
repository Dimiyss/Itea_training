from time import time, sleep
from typing import Any


def benchmark(method: Any, critical_time: float):
    """
    This is function for time execution calc
    :param method: Class method
    :param critical_time: critical time execution value in sec
    :return: func
    """
    def wrapper(*args, **kwargs):
        time_start = time()
        res = method(*args, **kwargs)
        if time() - time_start >= critical_time:
            print(f'WARNING! {method} slow!! Time is: {time() - time_start} sec, critical_time = {critical_time}')
        return res

    return wrapper


def decor_time_critical(critical_time: float):
    """
    External func decor for receiving critical timeout
    :param critical_time: critical time execution value in sec
    :return: internal func decorator
    """
    def decor_time_critical_without_time(cls):
        class DecorClass:
            """New Class that changed input class"""
            def __init__(self, *args, **kwargs):
                self._obj = cls(*args, **kwargs)

            def __getattribute__(self, item):
                try:
                    is_my_attribute = super().__getattribute__(item)
                except AttributeError:
                    pass
                else:
                    return is_my_attribute

                val_attr = self._obj.__getattribute__(item)

                if callable(val_attr):
                    return benchmark(val_attr, critical_time)
                else:
                    return val_attr

        return DecorClass

    return decor_time_critical_without_time


@decor_time_critical(0.5)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


t = Test()

t.method_1()
t.method_2()

# slow method start
# slow method finish
# WARNING! method_1 slow. Time = ??? sec.
# fast method start
# fast method finish
