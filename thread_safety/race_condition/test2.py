import threading

REPEAT = 10000000

x = 0

def increment():
    global x
    for _ in range(REPEAT):
        x += 1
def decrement():
    global x
    for _ in range(REPEAT):
        x -= 1

def main():
    global x
    x = 0
    
    thread1 = threading.Thread(target = increment)
    thread2 = threading.Thread(target = decrement)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'result: {x}')

if __name__=='__main__':
    main()