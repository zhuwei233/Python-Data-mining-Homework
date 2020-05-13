from threading import Thread
import time
def count_off():
    for a in range(1,11):
        print(a)
        time.sleep(0.5)
        


if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=count_off)
        t.start()
    while True:
        pass
