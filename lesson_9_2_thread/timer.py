from threading import Timer, Event
from time import sleep

e = Event()


def func():
    print('Hello from func')
    e.set()


if __name__ == '__main__':
    t = Timer(3, func)
    t.start()

    sleep(2)
    t.cancel()

    print('Finish!')
