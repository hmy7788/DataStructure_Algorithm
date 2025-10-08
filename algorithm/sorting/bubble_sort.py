def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr

print(bubble_sort([1, 0, 3, 2, 4]))