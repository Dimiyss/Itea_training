from time import time
import os
import urllib.request
from threading import Thread


def download_func(url):
    print(url)
    handle = urllib.request.urlopen(url)
    filename = os.path.basename(url)

    with open(f'./imgs/{filename}', 'wb') as f:
        while True:
            chunk = handle.read(1024)
            if not chunk:
                break
            f.write(chunk)
    print(f'{filename} download finished!')


urls = ['https://mirpozitiva.ru/wp-content/uploads/2017/12/013.jpg',
        'https://mirpozitiva.ru/wp-content/uploads/2017/12/2020-6.jpg',
        'https://mirpozitiva.ru/wp-content/uploads/2017/12/014.jpg',
        'https://mirpozitiva.ru/wp-content/uploads/2017/12/002.jpg',
        'https://mirpozitiva.ru/wp-content/uploads/2017/12/2020-1.jpg']

# start = time()
#
# for url in urls:
#     download_func(url)
#
# print(f'time: {time() - start} sec.')
# # time: 0.5867390632629395 sec.


# threads = []
#
# for url in urls:
#     th = Thread(target=download_func, args=(url,))
#     threads.append(th)
#
# # start threads
# start = time()
# for th in threads:
#     th.start()
#
# # wait finish threads
# for th in threads:
#     th.join()
#
# # time: 0.17350220680236816 sec.
# print(f'time: {time() - start} sec.')



def inc():
    num = 0
    for i in range(1000000):
        num += 1
    return num

# start = time()
# for th in range(10):
#     inc()
#
# # time: 0.4814176559448242 sec.
# print(f'time: {time() - start} sec.')

threads = []
for i in range(10):
    thread = Thread(target=inc)
    threads.append(thread)

# start threads
start = time()
for th in threads:
    th.start()

# wait finish threads
for th in threads:
    th.join()

# time: 0.5749542713165283 sec.
print(f'time: {time() - start} sec.')