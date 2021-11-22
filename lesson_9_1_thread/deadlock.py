import threading


l = threading.RLock()


def test():
    print('func test starting')

    with l:
        pass

    print('func test finished')


if __name__ == '__main__':
    with l:
        print('after acquire in main. Call test func...')

        test()

        print('after finish test func')