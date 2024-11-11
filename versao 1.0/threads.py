import threading
import time


def A(n, *args, **kwargs):
    while n > 1:
        n = n-1
        print(f'a{n}')
        time.sleep(1)


def B(n, *args, **kwargs):
    while n > 1:
        n = n-1
        print(f'b{n}')
        time.sleep(1)


def C(n, *args, **kwargs):
    while n > 1:
        n = n-1
        print(f'c{n}')
        time.sleep(1)


n = 10000


thread1 = threading.Thread(target=A, args=[n])
thread2 = threading.Thread(target=B, args=[n])
thread3 = threading.Thread(target=C, args=[n])


thread1.start()
thread2.start()
thread3.start()