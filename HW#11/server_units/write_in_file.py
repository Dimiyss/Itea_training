from multiprocessing import Process, Queue, Event


class WritePrime(Process):

    def __init__(self, queue: Queue, event: Event, path: str):
        super().__init__()
        self.queue = queue
        self.event = event
        self.path = path

    def run(self):

        while True:
            msg = self.read_que()
            if msg == 0:
                break
                
            self.write_file(f'{msg}\n')


        print('Writer ended')
        return None

    def read_que(self):
        return self.queue.get()

    def write_file(self, msg):
        with open(self.path, 'a') as file:
            file.write(msg)
