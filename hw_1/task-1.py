try:
    a_min = int(input('Please, enter min a value a_min:'))
except ValueError:
    print('You enter not integer value. To be used default -5')
    a_min = -5
try:
    a_max = int(input('Please, enter max a value a_max:'))
except ValueError:
    print('You enter not integer value. To be used default 1')
    a_max = 1
try:
    b_min = int(input('Please, enter min b value b_min:'))
except ValueError:
    print('You enter not integer value. To be used default -5')
    b_min = -5
try:
    b_max = int(input('Please, enter max b value b_max:'))
except ValueError:
    print('You enter not integer value. To be used default 1')
    b_max = 1
try:
    c_min = int(input('Please, enter min c value c_min:'))
except ValueError:
    print('You enter not integer value. To be used default -5')
    c_min = -5
try:
    c_max = int(input('Please, enter max c value c_max:'))
except ValueError:
    print('You enter not integer value. To be used default 1')
    c_max = 1


def task_solution(a1, a2, b1, b2, c1, c2):
    for a in range(a1, a2):
        for b in range(b1, b2):
            for c in range(c1, c2):
                d = (b ** 2) - (4 * a * c)
                if d < 0:
                    continue
                else:
                    try:
                        x1 = ((-1) * b + d ** 0.5) / (2 * a)
                        x2 = ((-1) * b - d ** 0.5) / (2 * a)
                        print(f'{a}, {b}, {c}, Yes, {x1}, {x2}')
                    except ZeroDivisionError:
                        print(f'{a}, {b}, {c}, Yes, -inf, inf')


task_solution(a_min, a_max, b_min, b_max, c_min, c_max)
