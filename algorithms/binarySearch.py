def searchElement (a, n, searchValue):
    first = 0
    last = n-1

    while first <=last:
        mid = (first + last)//2
        if searchValue < a[mid]:
            last = mid -1

        elif searchValue >a[mid]:
            first = mid+1

        else:
            return mid
    return -1


def binary_search (a, n, searchValue):
    return __search (a, 0,n-1, searchValue)


def __search(a ,first, last, searchValue):
    if (first > last):
        return -1
    mid = (first+last)//2
    if searchValue > a[mid]:
        return __search (a, mid+1 , last, searchValue)
    elif searchValue < a[mid]:
        return __search (a, first , mid -1, searchValue)
    else:
        return mid




n = int(input("Enter the num of elements"))
print "enter elements"
a =[None]*n
for i in range(n):
    a[i] = int(input("Enter element"))

searchValue = int(input("enter the searchElement"))
index = searchElement(a,n, searchValue)

if index == -1:
    print "value" , searchValue , "not found"
else:
    print "value", searchValue ,"found at index:", index
