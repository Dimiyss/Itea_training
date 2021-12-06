import sys
from multiprocessing import Manager, Semaphore
from server_units.server import Server
from server_units.validator import Validator
from server_units.write_in_file import WritePrime
import concurrent.futures as cf
from time import sleep


def start_server():
    with open('./server_units/test.txt', 'w') as f:
        f.write('')

    #sleep(0.1)
    m = Manager()
    event_finish_server = m.Event()
    event_finish_validator = m.Event()
    check_queue = m.Queue()
    dest_queue = m.Queue()
    server = Server(check_queue, event_finish_server)
    server.start()

    # validators = [Validator(check_queue, dest_queue, event_finish_server, event_finish_validator, i) for i in range(1)]
    valid = Validator(check_queue, dest_queue, event_finish_server, event_finish_validator, 0)

    # for valid in validators:
    #     valid.start()
    valid.start()

    writer = WritePrime(dest_queue, event_finish_validator, './server_units/test.txt')
    writer.start()
    #server.join()

    # check_queue.put(0)
    #print('Server_end_job')
    #writer.join()
    # for valid in validators:
    #     valid.join()

    valid.join()
    writer.join()
    sys.exit(0)
    server.join()



if __name__ == '__main__':
    start_server()
