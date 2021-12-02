
import numpy as np
import time


print("Configuration")
# Python float is 64 bit / 8 byte
ARRAY_SIZE = 1000 * 1000 * 10
print("- Size of data array: {} MB".format(ARRAY_SIZE * 8 / (1000 * 1000)))

N = 10
print("- Number of iterations to average: {}".format(N))

def SETUP():
    array1 = np.ones(ARRAY_SIZE)
    array2 = np.ones(ARRAY_SIZE)
    buffer_array = np.empty(ARRAY_SIZE)
    return array1, array2, buffer_array


if __name__=="__main__":

    print("{:45}{:<15}{:<15}".format("Case description", "Total time", "Per-iteration time"))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        for i in range(ARRAY_SIZE):
            array1[i] + array2[i]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("For-loop computation", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        [array1[i] + array2[i] for i in range(ARRAY_SIZE)]

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("List comprehension computation", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        for i in range(ARRAY_SIZE):
            buffer_array[i] = 2.0

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("For-loop list construction", elapsed_time, average))


    array1, array2, buffer_array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        buffer_array = np.array([2.0 for i in range(ARRAY_SIZE)])

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("List comprehension list construction", elapsed_time, average))
