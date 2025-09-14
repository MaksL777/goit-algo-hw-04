import random
import timeit


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

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
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    return sorted(arr)


def run_test(n=1000):
    arr = [random.randint(0, 10000) for _ in range(n)]

    print(f"\nТест для n = {n}")
    print("Insertion sort:", timeit.timeit(lambda: insertion_sort(arr), number=1))
    print("Merge sort:    ", timeit.timeit(lambda: merge_sort(arr), number=1))
    print("Timsort:       ", timeit.timeit(lambda: timsort(arr), number=1))

if __name__ == "__main__":
    for n in [100, 1000, 5000]:
        run_test(n)
