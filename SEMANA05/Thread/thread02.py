#Using threads - sleeping - two instances

""" import threading, time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1sec')
    time.sleep(1)
    print('Done Sleeping')

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
 """

#Using threads - sleeping - multiple instances

import threading, time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args= [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
