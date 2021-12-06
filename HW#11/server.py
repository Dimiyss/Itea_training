import sys
from multiprocessing import Manager
from server_units.server import Server
from server_units.validator import Validator
from server_units.write_in_file import WritePrime


def start_server():
    with open('./server_units/test.txt', 'w') as f:
        f.write('')

    m = Manager()
    event_finish_server = m.Event()
    event_finish_validator = m.Event()
    check_queue = m.Queue()
    dest_queue = m.Queue()
    server = Server(check_queue, event_finish_server)
    server.start()

    valid = Validator(check_queue, dest_queue, event_finish_server, event_finish_validator, 0)

    valid.start()

    writer = WritePrime(dest_queue, event_finish_validator, './server_units/test.txt')
    writer.start()

    valid.join()
    writer.join()
    sys.exit(0)
    server.join()


if __name__ == '__main__':
    start_server()
