import threading

REPEAT = 1000000

def main():
    x = 0

    def increment():
        nonlocal x
        for _ in range(REPEAT):
            x += 1
    def decrement():
        nonlocal x
        for _ in range(REPEAT):
            x -= 1
    
    thread1 = threading.Thread(target = increment)
    thread2 = threading.Thread(target = increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'result: {x}')

if __name__=='__main__':
    for _ in range(10):
        main()