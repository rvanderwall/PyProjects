import numpy as np
import psutil
import sys

# https://pythonspeed.com/articles/reduce-memory-array-copies/
#



def memory_usage(call_point):
    current_process = psutil.Process()
    memory = current_process.memory_info().rss
    print(int(memory / (1024*1024)), "MB", f" at {call_point}")

def load_1GB_of_data():
    return np.ones((2 **30), dtype=np.uint8)


def modify1(data):
    print("modify1 - refcount:",sys.getrefcount(data))
    memory_usage("in m1")
    return data * 2

def modify2(data):
    print("modify2 - refcount:",sys.getrefcount(data))
    memory_usage("in m2")
    return data + 10

# Peak 3GB
# naive
def process_data():
    print("-----  Process_data: a naive approach")
    memory_usage("before any allocation")
    data = load_1GB_of_data()
    memory_usage("after allocation")  # 1G
    print("process_data - refcount:", sys.getrefcount(data))
    m1 = modify1(data)
    memory_usage("after m1")          # 2G, data and m1
    m2 = modify2(m1)
    memory_usage("after m2")          # 3G, data and m1 and m2
    print("process_data - refcount:",sys.getrefcount(data))
    return m2

# Peak 3GB since anonymous array isn't deallocated until after the return
# data, modify1 anonymous local, modify3 anonymous local


def process_data_anonymous():
    print("-----  Process_data_anonymous: a better approach")
    memory_usage("before any allocation")
    data = load_1GB_of_data()
    memory_usage("after allocation")
    return modify2(modify1(data))   # Down to 2G peak


# Solution 1
# Anonymous result from load is freed once modify1 returns
def process_data_no_locals():
    print("-----  Process_data_no_locals: still cheaper approach")
    return modify2(modify1(load_1GB_of_data()))


# Solution 2
# Reuse local variabl
def process_data_reuse_locals():
    print("-----  Process_data_no_locals: still cheaper approach")
    memory_usage("before any allocation")
    data = load_1GB_of_data()
    memory_usage("after allocation")  # 1G
    print("process_data - refcount:", sys.getrefcount(data))
    data = modify1(data)
    memory_usage("after m1")          # 1G, data and m1
    data = modify2(data)
    memory_usage("after m2")          # 1G, data and m1
    print("process_data - refcount:", sys.getrefcount(data))
    return data


# Solution 3
# Transfer ownership in modify1 so we don't hold it
class Owner:
    def __init__(self, data):
        self.data = data

def process_data_owner():
    data = Owner(load_1GB_of_data())
    return modify2(modify1_owner(data))

def modify1_owner(owned_data):
    data = owned_data.data
    ownder_data.data = None
    return data * 2

def run():
    memory_usage("at start of run")
    #x = process_data()
    #x = process_data_anonymous()
    #x = process_data_no_locals()
    x = process_data_reuse_locals()
    memory_usage('at end of run')

if __name__ == "__main__":
    print("Memory usage examples")
    run()
    memory_usage('at end of main')
