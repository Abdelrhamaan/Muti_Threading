import threading
import time

players_name = ["aboody", "boody", "omar", "noor", "abozaid", "riko"]
players_number = len(players_name)
barrier = threading.Barrier(players_number)

def playing(name):
    score = 0
    for _ in range (3):
        print(f"{name} is playing")
        time.sleep(3)
    barrier.wait()
    print(f"{name} is scored {score}")
    print(f"sending winning amount to {name}")
    
    
my_threads = []    
for player in players_name:
    thread = threading.Thread(target=playing, args=(player,))
    my_threads.append(thread)
    thread.start()
