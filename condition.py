import threading
import math

con = threading.Condition()

def temperature():
    con.acquire()
    days = ['saturday', 'sunday', 'monday', 'tusday', 'wensday', 'thursday', 'friday']
    with open('temp.txt','w') as file:
        for day in days:
            temp = input(f'Enter Temperature of {day}')
            file.write(temp+'\n')
    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    con.wait(0)
    with open('temp.txt','r') as file:
        data = file.readlines()
        max = float(data[0].strip('\n'))
        for temp in data[1:]:
            temp = float(temp.strip('\n'))
            if temp > max:
                max = temp
    print(f"maximum temp is {max}")
    con.release()

def avg_temp():
    con.acquire()
    con.wait(0)
    with open('temp.txt',mode='r') as file:
        data = file.readlines()
        all_temp = [float(i.strip('\n'))for i in data]
        total = sum(all_temp)
        avg = math.floor(total/len(all_temp))
    print(f"avg temp is {avg}")
    con.release()

t1 = threading.Thread(target=temperature)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()
