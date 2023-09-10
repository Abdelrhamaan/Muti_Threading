import threading
import queue

my_queue = queue.Queue()

def producer(my_queue):
    print("Producer started")
    num = int(input("Enter number of students? "))
    for _ in range(num):
        mark = float(input("Enter student marks?  "))
        my_queue.put(mark)
    my_queue.put(None)
    print("Producer ended")
    


def consumer(my_queue):
    print("consumer started")
    while True:
        item = my_queue.get()
        if item == None:
            break
        print(f"mark is {item}")
    print("consumer ended")


t1 = threading.Thread(target = producer, args =(my_queue,))
t2 = threading.Thread(target = consumer, args =(my_queue,))

t1.start()
t2.start()