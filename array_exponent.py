
import numexpr as ne
import numpy as np
import time

print("Configuration")
# Python float is 64 bit / 8 byte
ARRAY_SIZE = 1000 * 1000 * 10
print("- Size of data array: {} MB".format(ARRAY_SIZE * 8 / (1000 * 1000)))

N = 100
print("- Number of iterations to average: {}".format(N))

def SETUP():
    array = np.ones(ARRAY_SIZE)
    return array


if __name__=="__main__":

    print("{:45}{:<15}{:<15}".format("Case description", "Total time", "Per-iteration time"))

    array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        _ = array * array * array * array

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Expanded", elapsed_time, average))


    array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        _ = np.power(array, 4)

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("np.power", elapsed_time, average))


    array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        _ = array ** 4

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("Intrinsic (**)", elapsed_time, average))


    array = SETUP()
    elapsed_time = 0.0
    for _ in range(N):
        start = time.time()

        _ = ne.evaluate("array ** 4")

        end = time.time()
        elapsed_time += end - start
    average = elapsed_time / N
    print("{:45}{:<15.6f}{:<15.6f}".format("numexpr", elapsed_time, average))
