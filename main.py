import numpy as np
import random
import timeit


def binary_search(np_array: np.array, target: int) -> None:
    found = False
    tmp_array = np_array
    while not found:
        mid_point = int(len(tmp_array) / 2)
        if tmp_array[mid_point] == target:
            found = True
            print('Number found traditionally!')
        else:
            found = False
        higher = True if tmp_array[mid_point] <= target else False
        tmp_array = tmp_array[mid_point:] if higher else tmp_array[:mid_point]
    return None


def recursive_binary(np_array: np.array, target: int) -> None:
    mid_point = int(len(np_array) / 2)
    if np_array[mid_point] == target:
        print('Number found recursively!')
        return None
    else:
        higher = True if np_array[mid_point] <= target else False
        tmp_array = np_array[mid_point:] if higher else np_array[:mid_point]
        recursive_binary(tmp_array, target)


def timing(function) -> None:
    start_time = timeit.default_timer()
    function
    print(f'Execution time: {timeit.default_timer() - start_time}')


if __name__ == '__main__':
    num_array = np.unique(np.random.randint(0, 1000, size=1000000))
    search = random.choice(num_array)
    timing(binary_search(num_array, search))
    timing(recursive_binary(num_array, search))
