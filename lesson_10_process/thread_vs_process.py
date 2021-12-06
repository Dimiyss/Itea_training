import time
import concurrent.futures as cf


def inc(n):
    num = 0
    for i in range(n):
        num += 1

    return num


if __name__ == '__main__':
    num = 0

    start = time.time()

    with cf.ProcessPoolExecutor(max_workers=10) as ex:
        for res in ex.map(inc, [1000000 for _ in range(10)]):
            num += res

    print(f'Time 10 threads = {time.time() - start}')
    print(f'num = {num}')