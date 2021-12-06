import math


def is_prime(num: int) -> bool:
    """Func that check if input value is prime

    :param num: number
    :return: True if number is prime else False
    """
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    sq = int(math.floor(math.sqrt(num)))
    for i in range(3, sq + 1, 2):
        if num % i == 0:
            return False

    return True
