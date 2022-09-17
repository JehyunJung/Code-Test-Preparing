from collections import deque
import time

def append_pop_list():
    arr=range(10**5)
    collection=[]

    start=time.time()
    for data in arr:
        collection.append(data)
    print("list append {}s".format(time.time()-start))

    start=time.time()
    for data in arr:
        collection.pop()
    print("list pop {}s".format(time.time()-start))

def insert_pop_list():
    arr=range(10**5)
    collection=[]

    start=time.time()
    for data in arr:
        collection.insert(0,data)
    print("list insertion {}s".format(time.time()-start))

    start=time.time()
    for data in arr:
        collection.pop(0)
    print("list pop(0) {}s".format(time.time()-start))

def appendleft_pop_deque():
    arr=range(10**5)
    collection=deque()
    
    start=time.time()
    for data in arr:
        collection.appendleft(data)
    print("deque insertion {}s".format(time.time()-start))

    start=time.time()
    for data in arr:
        collection.popleft()
    print("deque pop {}s".format(time.time()-start))


def append_pop_deque():
    arr=range(10**5)
    collection=deque()

    start=time.time()
    for data in arr:
        collection.append(data)
    print("deque append {}s".format(time.time()-start))

    start=time.time()
    for data in arr:
        collection.pop()
    print("deque pop {}s".format(time.time()-start))


insert_pop_list()
append_pop_list()
appendleft_pop_deque()
append_pop_deque()
