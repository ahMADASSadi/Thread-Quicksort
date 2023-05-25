import random
from threading import *
import time


def normal_quicksort(array, start, end):
    if start >= end:
        return

    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            #
        else:
            break

    array[start], array[high] = array[high], array[start]

    p = high
    normal_quicksort(array, start, p - 1)
    normal_quicksort(array, p + 1, end)


def thread_sort(sets, left, right):
    i = left
    j = right

    pivot = sets[int((left + right) / 2)]
    temp = 0
    while i <= j:
        while pivot > sets[i]:
            i = i + 1

        while pivot < sets[j]:
            j = j - 1

        if i <= j:
            temp = sets[i]
            sets[i] = sets[j]
            sets[j] = temp
            i = i + 1
            j = j - 1

    left_thread = None
    right_thread = None

    if left < j:
        left_thread = Thread(target=lambda: thread_sort2(sets, left, j))
        left_thread.start()

    if i < right:
        right_thread = Thread(target=lambda: thread_sort2(sets, i, right))
        right_thread.start()

    if left_thread is not None:
        left_thread.join()
    if right_thread is not None:
        right_thread.join()
    return sets


def thread_sort2(sets, left, right):
    i = left
    j = right

    pivot = sets[int((left + right) / 2)]
    temp = 0
    while i <= j:
        while pivot > sets[i]:
            i = i + 1

        while pivot < sets[j]:
            j = j - 1

        if i <= j:
            temp = sets[i]
            sets[i] = sets[j]
            sets[j] = temp
            i = i + 1
            j = j - 1

    left_thread = None
    right_thread = None

    if left < j:
        left_thread = Thread(target=normal_quicksort(sets, left, j))
        left_thread.start()

    if i < right:
        right_thread = Thread(target=normal_quicksort(sets, i, right))
        right_thread.start()

    if left_thread is not None:
        left_thread.join()
    if right_thread is not None:
        right_thread.join()
    return sets


ls = []
for i in range(10000000):
    ls.append(random.randint(9, 99999999999))

start = time.time()
thread_sort(ls, 0, len(ls) - 1)
end = time.time()

time1 = end - start
print(f"thread sort:{time1}")

random.shuffle(ls)

start2 = time.time()
normal_quicksort(ls, 0, len(ls) - 1)
end2 = time.time()
time2 = end2 - start2
print(f"normal sort:{time2}")
print(time2 - time1)
print(f"thread Vs. normal:{round(-(time1 - time2) * 100 / time2)}%")

