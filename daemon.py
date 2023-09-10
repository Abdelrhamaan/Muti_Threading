import threading
import time

# def display():
#     for i in range(10):
#         print("teaching session", i)
#         time.sleep(0.7)
    
# t1 = threading.Thread(target = display)
# """
# after that line when progrm is finished 
# daemon thread will finish and will not continue
# """
# t1.daemon = True 
# t1.start()
# # t1.join()
# time.sleep(3) # try to remove that line
# print("Exam Time !!!")
# print("Exam is over !!!!")


def syntax_highlight():
    for _ in range (10):
        print("highlight synatx")
        time.sleep(1)
        
t1 = threading.Thread(target = syntax_highlight)
t1.daemon = True
t1.start()
time.sleep(3)
print("close program")