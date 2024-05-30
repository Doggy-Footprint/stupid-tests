"""
gcore is used to dump memory

$ ps -ef | grep test_memory_cleanup.py -> get pid.
$ sudo gcore pid
$ ghex core.pid

or 
$ run dump_memory.sh <pid>
in another shell
"""


import time



if __name__ == '__main__':
    if 0:
        a = input('Input password: ')
        time.sleep(10000)
    if 0:
        a = input('pw1: ').encode()
        print('id of a: ', id(a))
        a = input('pw2: ')
        print('id of a: ', id(a))
        time.sleep(10000)
    if 1:
        with open('test_pw1', 'rb') as f1:
            a = bytearray(20)
            f1.readinto(a)
        with open('test_pw2', 'rb') as f2:
            b = bytearray(20)
            f2.readinto(b)
        c = input('Check both variables in memory dump.\nPress Enter to precede.')
        for i in range(20): a[i] = 0x30
        for i in range(20): b[i] = 0x31
        c = input('Check both variables not in memory dump.\nPress Enter to precede.')