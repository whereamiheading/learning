# ## Bubble sort O(n^2)
# def bubble_sort(arr):
#     for n in range(len(arr)-1, 0, -1):
#         for k in range(n):
#             if arr[k]>arr[k+1]: # Changing the > to < would reverse sort the array
#                 arr[k], arr[k+1] = arr[k+1], arr[k]
#
#     return arr
# output= bubble_sort([4,3,5, 1, 7, 9, 2,0])
# print output
#
##Selection Sort --> O(n^2)
def selection_sort(arr):
    for i in range(len(arr) ):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]: ## < -- ascending , > --- descending
                minIndex = j
        if minIndex != i:
            arr[i] , arr[minIndex] = arr[minIndex] , arr[i]
    return  arr
output = selection_sort([2,1,4,3,9,5,8,7,7,0])
print output
output = selection_sort([])
print output


def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] >a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]

    return a

op = bubble_sort([2,1,0,4,7,5])
print op


#better for small list and complexity is O(n^2)
def insert_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp
    return a
op = insert_sort([8,2,1,0,4,7,5,9])
print op


#merge_sort O(nlogn)
def merge_sorted_lists(l1, l2):
    sorted = []
    l1 = l1[:]
    l2 =l2[:]
    while l1 and l2:
        if l1[0] <=l2[0]:
            sorted.append(l1.pop(0))
        else:
            sorted.append(l2.pop(0))
    sorted.extend(l1 if l1 else l2)
    return sorted

def merge_sort(a):
    if len(a)<=1: return a

    left = merge_sort(a[:len(a)/2])
    right = merge_sort(a[len(a)/2:])

    return merge_sorted_lists(left, right)

print merge_sort([9,0,2,3,1,8,4])


##Udemy Way:

def merge_sortu(a1, a2 , temp ):
    i,j, k=0,0,0
    n1, n2 = len(a1),len(a2)
    while i <= n1-1 and j <= n2-1:
        if a1[i] < a2[j]:
            temp[k] = a1[i]
            i+=1
        else:
            temp[k] = a2[j]
            j+=1

        k+=1

    while i <= n1 -1:
        temp[k] = a1[i]
        i+=1
        k+=1

    while j<=n2-1:
        temp[k] = a2[j]
        j+=1
        k+=1
    return temp
a1 = [0,3,5,6,9]
a2 =[11,1,2,8,10]
temp = [None]*(len(a1)+len(a2))
#print merge_sortu(a1, a2, temp)

from random import randint

def quick_sort(a):
    if len(a)<=1: return a
    pivot = a[randint(0, len(a)-1)]
    smaller, equal, larger = [],[],[]
    for x in a:
        if x<pivot: smaller.append(x)
        elif x==pivot: equal.append(x)
        else: larger.append(x)

    return quick_sort(smaller)+equal +quick_sort(larger)
print 'quick'
print quick_sort ([2,3,1,9,0])
