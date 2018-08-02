a = [2,5,0]
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

#print merge_sort([9,0,2,3,1,8,4])

#Selection_sort:

def select(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j]<a[min]:
                min =j
        if i!= min:
            a[min], a[i] = a[i], a[min]
    return a

print select(a)

def bubble(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print bubble(a)

def insert(a):
    for i in range(len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
    return a
print insert(a)

def merge(l1, l2):
    l1 =l1[:]
    l2 =l2[:]
    sorted =[]
    while l1 and l2:
        if l1[0] < l2[0]: sorted.append(l1.pop(0))
        else:   sorted.append(l2.pop(0))
    sorted.extend(l1 if l1 else l2)
    return sorted

def merge_sort(a):
    if len(a) ==1: return a

    left = merge_sort(a[:len(a)/2])
    right = merge_sort(a[len(a)/2:])

    return merge(left, right)
print merge_sort([4,3,6,0])

from random import randint
def quick(a):
    if len(a) <=1: return a
    smaller, larger , equal =[],[],[]
    pivot_e = a[randint(0, len(a)-1)]

    for x in a:
        if x>pivot_e: larger.append(x)
        elif x==pivot_e: equal.append(x)
        else: smaller.append(x)
    return quick(smaller)+equal +quick(larger)

print quick(a)
