import time
import concurrent.futures as cf


def inc(n):
    num = 0

    for i in range(n):
        num += 1

    return num


if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        inc(1000000)
    print(f'Time one thread = {time.time() - start}')


    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        ex.map(inc, [1000000 for _ in range(10)])
    print(f'Time 10 threads = {time.time() - start}')


    start = time.time()
    with cf.ProcessPoolExecutor(max_workers=10) as ex:
        ex.map(inc, [1000000 for _ in range(10)])
    print(f'Time 10 pocesses = {time.time() - start}')

# Time one thread = 0.43500232696533203
# Time 10 threads = 0.5235946178436279
# Time 10 pocesses = 0.33451008796691895