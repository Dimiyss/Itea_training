from random import randint
import concurrent.futures as cf
from threading import Lock

MSG_FINISH = object()
l = Lock()

setM = 0
getM = 0


class Pipeline:
    def __init__(self):
        self.msg = 0

        self.producer_lock = Lock()
        self.consumer_lock = Lock()

        self.consumer_lock.acquire()

    def set_msg(self, msg):
        self.producer_lock.acquire()
        self.msg = msg
        self.consumer_lock.release()

    def get_msg(self):
        self.consumer_lock.acquire()
        ret = self.msg
        self.producer_lock.release()
        return ret


def producer(pipeline: Pipeline):
    global setM

    for i in range(10):
        msg = randint(1, 100)

        pipeline.set_msg(msg)
        print(f'Producer got message: {msg}')
        setM += 1

    pipeline.set_msg(MSG_FINISH)


def consumer(pipeline: Pipeline):
    global getM
    msg = None

    while msg is not MSG_FINISH:
        msg = pipeline.get_msg()

        if msg is not MSG_FINISH:
            getM += 1
            print(f'Consumer read message: {msg}')


if __name__ == '__main__':
    pipeline = Pipeline()

    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)

print(f'setM = {setM}')
print(f'getM = {getM}')

# 36 32 63 79 29 35 81 94 95 45
# 36 32 63 79 29 35 81 94 95 45
