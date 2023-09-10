import threading
import time

event = threading.Event()


def traffic_light():
    while True:
        print("light is green")  # true
        event.set()  # flag = true --- send msg (you can go)
        time.sleep(5)
        print('light is red stop!!')  # print this and stop (you can go)
        event.clear()  # flag = false
        time.sleep(5)
        event.set()  # flag = true


def msg():
    event.wait()
    while event.is_set():
        print("you can go...")
        time.sleep(0.5)
        event.wait()


t1 = threading.Thread(target=traffic_light)
t2 = threading.Thread(target=msg)

t1.start()
t2.start()
