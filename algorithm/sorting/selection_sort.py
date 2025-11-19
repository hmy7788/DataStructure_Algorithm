from sort_utils import swap

def selection_sort(arr: list):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)

    return arr

print(selection_sort([1, 0, 3, 2, 4]))