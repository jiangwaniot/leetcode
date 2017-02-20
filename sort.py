import random
from random import randrange


def bubble_sort(seq):
    L = len(seq)
    for i in range(L):
        for n in range(1, L - i):
            if seq[n] < seq[n - 1]:
                seq[n], seq[n - 1] = seq[n - 1], seq[n]
    return seq


def select_sort(seq):
    for i in range(len(seq)):
        tmp = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[tmp]:
                tmp = j
        if tmp != i:
            seq[tmp], seq[i] = seq[i], seq[tmp]
    return seq


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] < right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1
    result += left[n:]
    result += right[m:]
    return result


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for i in seq[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_inplace(seq, left, right):
    if len(seq) <= 1:
        return seq
    elif left < right:
        pivot = randrange(left, right)
        pivot_new_index = partition(seq, left, right, pivot)
        quick_sort_inplace(seq, left, pivot_new_index - 1)
        quick_sort_inplace(seq, pivot_new_index + 1, right)


# https://upload.wikimedia.org/wikipedia/commons/8/84/Lomuto_animated.gif
def partition(seq, left, right, pivot_index):
    pivot_value = seq[pivot_index]
    seq[right], seq[pivot_index] = seq[pivot_index], seq[right]
    store_index = left
    for i in range(left, right):
        if seq[i] < pivot_value:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


def counting_sort(seq, k):
    count = [0] * (k + 1)
    for i in range(len(seq)):
        count[seq[i]] += 1
    p = 0
    for i in range(k + 1):
        for j in range(count[i]):
            seq[p] = i
            p += 1
    return seq


test = list(range(20)) * 10
random.shuffle(test)
# print(test)
if bubble_sort(test) != sorted(test):
    print(test)
    print(bubble_sort(test))
    print(sorted(test))
else:
    print("bubble_sort yes")

if select_sort(test) != sorted(test):
    print(test)
    print(select_sort(test))
    print(sorted(test))
else:
    print("select_sort yes")

if merge_sort(test) != sorted(test):
    print(test)
    print(merge_sort(test))
    print(sorted(test))
else:
    print("merge_sort yes")

if quick_sort(test) != sorted(test):
    print(test)
    print(quick_sort(test))
    print(sorted(test))
else:
    print("quick_sort yes")

# print(test)
quick_sort_inplace(test, 0, len(test) - 1)
# print(test)
if test != sorted(test):
    print(test)
    print(quick_sort_inplace(test, 0, len(test) - 1))
    print(sorted(test))
else:
    print("quick_sort_inplace yes")

if counting_sort(test, 20) != sorted(test):
    print(test)
    print(counting_sort(test))
    print(sorted(test))
else:
    print("counting_sort yes")
