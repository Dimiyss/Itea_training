from threading import Semaphore

sem = Semaphore(3)

print('before 1 acquire')
sem.acquire()
print('after 1 acquire\n')

print('before 2 acquire')
sem.acquire()
print('after 2 acquire\n')

print('before 3 acquire')
sem.acquire()
print('after 3 acquire\n')

# sem.acquire()
# print('!!!!')

sem.release()
sem.release()


print('before 4 acquire')
sem.acquire()
print('after 4 acquire\n')

print('before 5 acquire')
sem.acquire()
print('after 5 acquire\n')