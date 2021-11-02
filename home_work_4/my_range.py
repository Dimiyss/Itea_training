class MyRange:
    """My class that delivery funcionality same as range func logic"""

    def __init__(self, first_arg: int, second_arg: int = None, step: int = 1) -> None:
        """
        :param first_arg: if second_arg not entered - stop value, else - start value
        :param second_arg: stop value
        :param step: step value
        """
        self.end = first_arg if second_arg is None else second_arg
        self.start = -1 if second_arg is None else (first_arg - step)
        self.step = step
        if self.step == 0:
            raise ValueError('Arg 3 must be not equal 0')

    def __iter__(self):
        return self

    def main_order(self) -> int:
        """
        Main order calc func
        :return: next value, or StopIteration
        """
        self.start += self.step
        if self.start < self.end:
            return self.start
        else:
            raise StopIteration

    def revers_order(self) -> int:
        """
        Reverse order calc func
        :return: next value, or StopIteration
        """
        self.start += self.step
        if self.start > self.end:
            return self.start
        else:
            raise StopIteration

    def __next__(self):
        if self.step > 0:
            return self.main_order()
        else:
            return self.revers_order()
