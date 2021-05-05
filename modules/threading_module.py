import logging
import time
import random

import threading

print("Thread")
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.info("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=(1,))
logging.info("Main    : before running thread")
x.start()
logging.info("Main    : wait for the thread to finish")
logging.info("Main    : all done")

# daemon
print("Daemon thread")
y = threading.Thread(target=thread_function, args=(2,), daemon=True)
y.start() # won`t show finishing message, because works on the background

print(threading.active_count()) # Output: 3
print(threading.current_thread())
print(threading.enumerate()) # return list of threads

# optional, for showing the daemon finishing message
# wait untill thread is not finished
# y.join()

time.sleep(5)

# lock
print("Lock")
x = 8192

# without locking thread, two or more thread will
# work in the same time, for the next example:
# Output:
# 16384.0
# 8192.0
# 16384.0
# 8192.0
# ...
lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()

    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)

    print('Reached the maximum')
    lock.release()

def halve():
    global x, lock
    lock.acquire()

    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)

    print("Reached the minimum")
    lock.release()

double_thread = threading.Thread(target=double)
halve_thread = threading.Thread(target=halve)

double_thread.start()
halve_thread.start()

time.sleep(20)

# Semaphore
print("Semaphore")

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

for thread_number in range(1, 11):
    access_thread = threading.Thread(target=access, args=(thread_number,))
    access_thread.start()
    time.sleep(1)

time.sleep(20)

# Event
print("Event")

event = threading.Event()

def event_function():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Performing action XYZ now...")

event_function_thread = threading.Thread(target=event_function)
event_function_thread.start()

x = input("Do you want to trigger the event? (y/n)\n")

if x == "y":
    event.set()

time.sleep(10)

# excepthook
print("excepthook")

def excepthook_impl(message):
    print(f"In excepthook: {message.exc_value}")

threading.excepthook = excepthook_impl

def error(timeout):
    time.sleep(timeout)
    raise Exception("Time is up!")

my_thread = threading.Thread(target=error, args=(3,))
my_thread.start()
time.sleep(7)

# Timer
print("Timer")

def hello():
    print("hello!")

hello_timer = threading.Timer(30, hello)
hello_timer.start() # after 30 seconds will show message: 'hello!'

# Barrier
def f(b):
    time.sleep(random.randint(2, 10))
    print("{} woke at: {}".format(threading.current_thread().getName(), time.ctime()))
    b.wait()
    print("{} passed the barrier at: {}".format(threading.current_thread().getName(), time.ctime()))

# Barrier object is created by using Barrier class which is available in the threading module.
# This object can be used where we want a set of threads to wait for each other.
#
# For example, if we have two threads and we want both the threads to execute when both are ready.
# In such situation both the threads will call the wait() method on the barrier object once they are ready
# and both the threads will be released simultaneously only when both of them have called the wait() method.

barrier = threading.Barrier(3)

for i in range(3):
    t = threading.Thread(target=f, args=(barrier,))
    t.start()