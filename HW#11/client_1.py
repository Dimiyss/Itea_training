from socket import socket
from client_units.msgutils import send_msg, default_encoding
from client_units.prime_genrator import gen_primes
from threading import Semaphore
from time import time, sleep



def start_client():
    sleep(1)
    start_time = time()
    #print(f'Client start {start_time}')
    #sem = Semaphore(2)
    # with cf.ThreadPoolExecutor(max_workers=10) as ex:
    #     for num in range(10):
    #         ex.submit(send_prime, num)
    send_prime(1)
    print(f'Client time = {time() - start_time}')


def send_prime(number):
    with socket() as sock:
        sock.connect(('localhost', 12345))

        #sem.acquire()
        for prime in gen_primes():
            # str_prime = str(prime)
            if prime:
                send_msg(f'{prime}'.encode(default_encoding), sock)
                #print(f'{prime} thread_num {number}')
            else:
                send_msg('End'.encode(default_encoding))
       # sem.release()


if __name__ == '__main__':
    start_time = time()
    start_client()
    sem = Semaphore(2)
    print(f' Transceiver work time = {time() - start_time}')
