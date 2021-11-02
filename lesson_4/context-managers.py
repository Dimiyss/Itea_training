class Res:
    def __init__(self, name):
        print(f'Resource {name} created')
        self.name = name

    def get_name(self):
        return self.name

    def post_work(self):
        print(f'Resource {self.name} closed')


class ResWorker:
    def __init__(self, name):
        self.__res = Res(name)

    def __enter__(self):
        return self.__res

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exc_type = {exc_type}')
        print(f'exc_val = {exc_val}')
        print(f'exc_tb = {exc_tb}')

        self.__res.post_work()


db = Res('DB')
with ResWorker('DB') as db:
    print(db.get_name())
    int(db)
