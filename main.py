import timeit
import random


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def timsort(arr):
    return sorted(arr)


def algorithm_testing(algorithm, data):
    setup_code = f"from __main__ import {algorithm}"
    stmt_code = f"{algorithm}({data})"
    time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=1000)
    return time


def main():
    data = [random.randint(0, 1000) for _ in range(1000)]

    merge_sort_time = algorithm_testing("merge_sort", data.copy())
    print("Merge Sort Time:", merge_sort_time, " seconds")

    insert_sort_time = algorithm_testing("insert_sort", data.copy())
    print("Insertion Sort Time:", insert_sort_time, " seconds")

    timsort_time = algorithm_testing("timsort", data.copy())
    print("Timsort Time:", timsort_time, " seconds")


if __name__ == "__main__":
    main()
