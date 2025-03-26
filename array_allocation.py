import numpy as np
import time
import sys
from memory_profiler import memory_usage

# Python float is 64 bit / 8 byte
ARRAY_SIZE = 1000 * 1000 * 10
print("- Size of data array: {} MB".format(ARRAY_SIZE * 8 / (1000 * 1000)))

def allocate_empty():
    a = np.empty( (ARRAY_SIZE) )

if __name__=="__main__":

    print(memory_usage((allocate_empty, (), {})))



# https://fa.bianp.net/blog/2013/different-ways-to-get-memory-consumption-or-lessons-learned-from-memory_profiler/
# https://pypi.org/project/memory-profiler/

