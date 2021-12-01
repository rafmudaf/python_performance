
import gc
import numpy as np
import time

# contiguous_array[i-1]
# contiguous_array[i]
# contiguous_array[i+1]
# new_array1 = np.ones(np.shape(contiguous_array))

print("Configuration")
# Python float is 64 bit / 8 byte
ARRAY_SIZE = 1000 * 1000 * 1
print("- Size of data array: {} MB".format(ARRAY_SIZE * 8 / (1000 * 1000)))

N = 10
print("- Number of iterations to average: {}".format(N))

def SETUP():
    array1 = np.ones(ARRAY_SIZE)
    array2 = np.ones(ARRAY_SIZE)
    buffer_array = np.empty(ARRAY_SIZE)
    return array1, array2, buffer_array


if __name__=="__main__":
    # gc.disable()

    print("{:45}{:<15}{:<15}".format("Case description", "Total time", "Per-iteration time"))
    
    array1, array2, buffer_array = SETUP()
    index_map = np.random.randint(0, ARRAY_SIZE - 1, size=ARRAY_SIZE)
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        for i in index_map:
            buffer_array[i] = array1[i] + array2[i]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Non-contiguous access, no vectorization", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        for i in range(ARRAY_SIZE):
            buffer_array[i] = array1[i] + array2[i]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Contiguous access, no vectorization", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    index_map = np.random.randint(0, ARRAY_SIZE - 1, size=ARRAY_SIZE)
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        buffer_array = array1[index_map] + array2[index_map]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Non-contiguous access, vectorization", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    index_map = np.arange(0, ARRAY_SIZE)
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        buffer_array = array1[index_map] + array2[index_map]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Contiguous access, vectorization", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        buffer_array = array1 + array2

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Numpy arithmetic", elapsed_time, average))
