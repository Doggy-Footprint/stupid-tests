import threading
import time

# Function to demonstrate a deadlock
def thread1_func():
    print("Thread 1: Attempting to acquire lock1")
    lock1.acquire()
    print("Thread 1: Acquired lock1")

    print("Thread 1: doing sth with lock1")

    control_event.wait()

    print("Thread 1: Attempting to acquire lock2 holding lock1") # dead-lock
    lock2.acquire()
    print("Thread 1: Acquired lock2, releasing lock1")
    lock1.release()

    print("Thread 1: doing sth with lock2")

    print("Thread 1: job done. Releasing lock2")
    lock2.release()

    print("Thread 1: quiting")



def thread2_func():
    print("Thread 2: Attempting to acquire lock2")
    lock2.acquire()
    print("Thread 2: Acquired lock2")

    print("Thread 2: doing sth with lock2")

    control_event.wait()

    print("Thread 2: Attempting to acquire lock1 holding lock2") # dead-lock
    lock1.acquire()
    print("Thread 2: Acquired lock1, releasing lock2")
    lock2.release()

    print("Thread 2: doing sth with lock1")

    print("Thread 2: job done. Releasing lock1")
    lock1.release()

    print("Thread 2: quiting")

# Create two locks
control_event = threading.Event()

lock1 = threading.Lock()
lock2 = threading.Lock()

# Create two threads
thread1 = threading.Thread(target=thread1_func)
thread2 = threading.Thread(target=thread2_func)

control_event.set()
# Start the threads
thread1.start()
thread2.start()

# wait for each thread to acquire lock
time.sleep(1)
# release event to let each thread run remaining parts, which is designed to occuring dead-lock
control_event.clear()

print("Wait for each thread to join - but will never end")

# Wait for the threads to complete
thread1.join()
thread2.join()

print("This will never be printed because of deadlock")