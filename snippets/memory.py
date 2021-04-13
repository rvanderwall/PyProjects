import numpy as np
import psutil

# https://pythonspeed.com/articles/reduce-memory-array-copies/
#



def memory_usage():
    current_process = psutil.Process()
    memory = current_process.memory_info().rss
    print(int(memory / (1024*1024)), "MB")

def load_1GB_of_data():
    return np.ones((2 **30), dtype=np.uint8)


def modify1(data):
    return data * 2

def modify2(data):
    return data + 10

# Peak 3GB
# naive
def process_data():
    memory_usage()
    data = load_1GB_of_data()
    memory_usage()
    m1 = modify1(data)
    memory_usage()
    m2 = modify2(m1)
    memory_usage()

# Peak 3GB since anonymous array isn't deallocated until after the return
# data, modify1 anonymous local, modify3 anonymous local
def process_data_anonymous():
    memory_usage()
    data = load_1GB_of_data()
    memory_usage()
    return modify2(modify1(data))


# Solution 1
# Anonymous result from load is freed once modify1 returns
def process_data_no_locals():
    return modify2(modify1(load_1GB_of_data()))


# Solution 2
# Reuse local variabl
def process_data_reuse_local():
    data = load_1GB_of_data()
    data = modify1(data)
    data = modify2(data)
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
    memory_usage()
    #x = process_data()
    x = process_data_anonymous()
    memory_usage()

if __name__ == "__main__":
    run()
