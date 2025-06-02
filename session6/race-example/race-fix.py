from threading import Thread,Lock
from time import sleep
data = [1,2,3]
data_lock = Lock()
def handle_data():
    while True:
        data_lock.acquire()
        if len(data)>0:
            sleep(0.1)
            print(data.pop(0))
            data_lock.release()
        else:
            data_lock.release()
            break
t1 = Thread(target=handle_data)
t2 = Thread(target=handle_data)
t1.start()
t2.start()
t1.join()
t2.join()
