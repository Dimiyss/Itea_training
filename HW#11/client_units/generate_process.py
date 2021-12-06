from multiprocessing import Process, Queue
from .prime_genrator import gen_primes


class PrimeGenerator(Process):

    def __init__(self, gen_queue: Queue):
        super().__init__()
        self.gen_queue = gen_queue

    def run(self) -> None:
        for prime in gen_primes():
            self.gen_queue.put(prime)

        self.gen_queue.put(0)
        self.gen_queue.put(0)
        self.gen_queue.put(0)
