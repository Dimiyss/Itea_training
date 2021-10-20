a1 = int(input('Please, enter min a value '))
a2 = int(input('Please, enter max a value '))
b1 = int(input('Please, enter min b value '))
b2 = int(input('Please, enter max b value '))
c1 = int(input('Please, enter min c value '))
c2 = int(input('Please, enter max c value '))

for a in range(a1, a2):
    for b in range(b1, b2):
        for c in range(c1,c2):
            d = (b ** 2) - (4 * a * c)
            if d >= 0:
                try:
                    x1 = ((-1) * b + d ** 0.5) / (2 * a)
                    x2 = ((-1) * b - d ** 0.5) / (2 * a)
                    print(f'{a}, {b}, {c}, Yes, {x1}, {x2}')
                except ZeroDivisionError:
                    print(f'{a}, {b}, {c}, Yes, -inf, inf')
            else:
                continue





