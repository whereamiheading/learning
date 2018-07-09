## Bubble sort
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k]>arr[k+1]: # Changing the > to < would reverse sort the array
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr
output= bubble_sort([4,3,5, 1, 7, 9, 2,0])
print output

##Selection Sort
def selection_sort(arr):
    for i in range(len(arr) -1 ):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[minIndex]: ## < -- ascending , > --- descending
                minIndex = j
        if minIndex != i:
            arr[i] , arr[minIndex] = arr[minIndex] , arr[i]
    return  arr
output = selection_sort([2,1,4,0,9,5])
print output
