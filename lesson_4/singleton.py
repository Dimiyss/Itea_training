class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        print('hello')



def test_func():
    s3 = Singleton()
    print(s3)


if __name__ == "__main__":
    # Клиентский код.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    print(s1)
    print(s2)

    test_func()
