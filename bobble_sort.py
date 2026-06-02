question on bobble sort by strings
"""bobble sort



def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr

arr = ["Rahul", "Amith", "Sneha", "Priya","Kiran"]
sorted = bubble(arr)
print("sorted array:", sorted)
