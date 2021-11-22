from multiprocessing import Process
from time import sleep


def func():
    i = 0
    while True:
        print(i)
        i += 1
        sleep(0.1)


if __name__ == '__main__':
    pr = Process(target=func, daemon=True)
    pr.start()

    sleep(1)
