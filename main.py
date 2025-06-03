import timeit
import random
from copy import deepcopy

# Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання.
# Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних.
# Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах.
# Для заміру часу виконання алгоритмів використовуйте модуль timeit.
#
# Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим,
# і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі.
# Зробіть висновки.


def merge_sorting(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sorting(left_half), merge_sorting(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def test_sorting_algorithms():
    sizes = [100, 1000, 5000, 10_000]
    results = {}

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]

        data_merge = deepcopy(data)
        data_insert = deepcopy(data)
        data_builtin = deepcopy(data)

        t_merge = timeit.timeit(lambda: merge_sorting(data_merge), number=1)
        t_insert = timeit.timeit(lambda: insertion_sort(data_insert), number=1)
        t_builtin = timeit.timeit(lambda: sorted(data_builtin), number=1)

        results[size] = {
            "merge_sort": t_merge,
            "insertion_sort": t_insert,
            "timsort_sorted": t_builtin,
        }

    return results


results = test_sorting_algorithms()

for size, timings in results.items():
    print(f"\nРозмір масиву: {size}")
    for algo, t in timings.items():
        print(f"{algo}: {t:.6f} секунд")

