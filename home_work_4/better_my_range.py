class MyRange:
    def __init__(self, start: int, stop: int = None, step: int = 1) -> None:
        if step == 0:
            raise ValueError('MyRange() arg 3 must not be zero')
        else:
            self.__step = step


        if stop is None:
            self.__start, self.__stop = 0, start
        else:
            self.__start, self.__stop = start, stop


    def __iter__(self):
        return self


    def __next__(self):
        ret = self.__start
        self.__start += self.__step


        if self.__step > 0 and ret < self.__stop \
                or self.__step < 0 and ret > self.__stop:
            return ret
        else:
            raise StopIteration