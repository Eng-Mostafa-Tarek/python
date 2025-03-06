import threading
import time

lock = threading.Lock()


def print_num():
    for num in range(5):
        time.sleep(1)
        with lock:
            print(f"number {num}")


def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        with lock:
            print(f"letter {letter}")


thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
