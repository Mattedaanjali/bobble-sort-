#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [3, 6, 8,2, 1, 4, 20]
sorted_arr = selection_sort(arr) 
print("sorted array:", sorted_arr)   