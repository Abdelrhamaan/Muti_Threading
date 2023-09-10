import threading
import time


def playing(name):
    score = 0
    for _ in range(3):
        print(f"{name} is playing")
        time.sleep(3)

    print(f"{name} is scored {score}")
    print(f"sending winning amount to {name}")


my_threads = []
players_name = ["aboody", "boody", "omar", "noor", "abozaid", "riko"]
for player in players_name:
    thread = threading.Thread(target=playing, args=(player,))
    my_threads.append(thread)
    thread.start()
