def my_range_func(first_param: int, second_param: int = None, step: int = 1) -> int:
    """
    My range iterator
    :param first_param: if second_param not entered - stop value, else - start value
    :param second_param: stop value
    :param step: step value
    :return: next iteration value
    """
    if step == 0:
        raise ValueError('Arg 3 must be not equal 0')

    if second_param is None:
        first_param, second_param = 0, first_param

    while (first_param - second_param) * step < 0:
        yield first_param

        first_param += step
