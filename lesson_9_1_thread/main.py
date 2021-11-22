from threading import Thread
import time


# def thread_func(num):
#     print(f'function #{num} starting')
#     time.sleep(1)
#     print(f'function #{num} finished')

class MyThread(Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    def run(self) -> None:
        print(f'function #{self.num} starting')
        time.sleep(1)
        print(f'function #{self.num} finished')


threads = []
for i in range(5):
    thread = MyThread(i)
    threads.append(thread)

# start threads
start = time.time()
for th in threads:
    th.start()

# wait finish threads
for th in threads:
    th.join()

print(f'time: {time.time() - start} sec.')