from contextlib import contextmanager

class Resource:
    def __init__(self, name):
        print(f'Resource: created {name}')
        self.__name = name

    def get_name(self):
        return self.__name

    def post_work(self):
        print('Resource: closed!')


@contextmanager
def ResourceWith(*args):
    try:
        obj = Resource(*args)
        yield obj
    except:
        pass
    finally:
        obj.post_work()


with ResourceWith('worker') as r:
    print(f'name: {r.get_name()}')