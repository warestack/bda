from threading import Thread
from time import sleep

data = [1,2,3]
def handle_data():
    while len(data)>0:
        sleep(0.5)
        print(data.pop(0))

t1 = Thread(target=handle_data)
t2 = Thread(target=handle_data)

t1.start()
t2.start()

t1.join()
t2.join()
