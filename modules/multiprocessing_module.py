import os
import time
import logging
import multiprocessing

# Logger multiprocessing
multiprocessing.log_to_stderr()

logger = multiprocessing.get_logger()
logger.setLevel(logging.INFO)

# Process
print("Process")

def doubler(number):
    """
    Функция умножитель на два
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))

numbers = [5, 10, 15, 20, 25]
procs = []

for index, number in enumerate(numbers):
    proc = multiprocessing.Process(target=doubler, args=(number,))
    print(f'{multiprocessing.current_process()}')
    procs.append(proc)
    proc.start()

for proc in procs:
    proc.join()

time.sleep(3)

# Lock
print("Lock")

def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

lock = multiprocessing.Lock()
items = ['tango', 'foxtrot', 10]

for item in items:
    p = multiprocessing.Process(target=printer, args=(item, lock))
    p.start()

time.sleep(3)

# Pool
print("Pool")

def doubler(number):
    return number * 2

numbers = [5, 10, 20]

# The pool allows you to do multiple jobs per process,
# which may make it easier to parallelize your program.
# If you have a million tasks to execute in parallel,
# you can create a Pool with a number of processes as many as
# CPU cores and then pass the list of the million tasks to pool.
pool = multiprocessing.Pool(processes=3)

print(pool.map(doubler, numbers))

time.sleep(3)

# Pool apply_async
print("Pool apply_async")

def doubler(number):
    return number * 2

pool = multiprocessing.Pool(processes=3)
result = pool.apply_async(doubler, (25,))
print(result.get(timeout=1))

time.sleep(5)

# Queue
print("Queue")

sentinel = -1

def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:
        q.put(item)


def my_consumer(q):
    """
    Consumes some data and works on it
    In this case, all it does is double the input
    """
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))

        processed = data * 2
        print(processed)

        if data is sentinel:
            break


q = multiprocessing.Queue()
data = [5, 10, 13, -1]

process_one = multiprocessing.Process(target=creator, args=(data, q))
process_two = multiprocessing.Process(target=my_consumer, args=(q,))

process_one.start()
process_two.start()

q.close()
q.join_thread()

process_one.join()
process_two.join()