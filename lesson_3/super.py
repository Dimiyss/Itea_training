class Base:
    def __init__(self):
        print('Base class created')


class ChildA(Base):
    def __init__(self):
        print('Class ChildA created')
        # Base.__init__(self)
        super().__init__()


class ChildB(Base):
    def __init__(self):
        print('Class ChildB created')
        # Base.__init__(self)
        super().__init__()



class ChildChild(ChildA, ChildB):
    def __init__(self):
        super(ChildChild, self).__init__()

        # for i in range(1, len(ChildChild.mro())):
        #     ChildChild.mro()[i].__init__(self)

        print('Class ChildChild created')
