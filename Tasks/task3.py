from array import *
from heapq import heappop, heappush

origin_arr = array('i')
size = int(input())
for i in range(size):
    origin_arr.insert(i, int(input()))


def arr_sort(arr):
    heap = []
    for elem in arr:
        heappush(heap, elem)
    sorted_arr = []
    while heap:
        sorted_arr.append(heappop(heap))
    return sorted_arr


print(arr_sort(origin_arr))

# Использовал метод сортиворки кучами, так как его ассимптотическая сложность наиболее приближена к теоретическому
# нижнему пределу
