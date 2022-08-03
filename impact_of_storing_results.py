
import numpy as np
import timeit


# Python float is 64 bit / 8 byte
array_size = 1000 * 1000 * 10
print("Size of data array: {} MB".format(array_size * 8 / (1000 * 1000)))

N = 10

SETUP = """
array1 = np.ones(array_size)
array2 = np.ones(array_size)
buffer_array = np.empty(array_size)
"""


print("### Storing")
index_map = np.arange(0, array_size)
def storing(array1, array2):
    buffer_array = array1[index_map] + array2[index_map]
    # return buffer_array

total_time = timeit.timeit(
    "storing(array1, array2)",
    number=10,
    setup=SETUP,
    globals=globals()
)
print(total_time / N)


print("### Not storing")
index_map = np.arange(0, array_size)
def not_storing(array1, array2):
    array1[index_map] + array2[index_map]

total_time = timeit.timeit(
    "not_storing(array1, array2)",
    number=10,
    setup=SETUP,
    globals=globals()
)
print(total_time / N)
