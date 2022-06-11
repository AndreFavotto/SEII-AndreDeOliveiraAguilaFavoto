#Synchronous function - sleeping

import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1sec')
    time.sleep(1)
    print('Done Sleeping')

do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

