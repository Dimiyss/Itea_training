def to_int(value):
    try:
        int_val = int(value)
    except ValueError:
        return 'Wrong choice, please repeat'

    return int_val
