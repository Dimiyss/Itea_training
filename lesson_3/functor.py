class Foo:
    def __call__(self, *args, **kwargs):
        print('this is call')


c = Foo()
c()