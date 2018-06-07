def searchElement(arr, searchValue):
    first = 0
    last = len(arr)-1

    while first <= last:
        mid = (first +last)//2
        if searchValue < arr[mid]:
            last = mid -1
        elif searchValue > arr[mid]:
            first = mid + 1
        else:
            return mid
    return -1







n = int(input("Enter the num of elements"))
print "enter elements"
a =[None]*n
for i in range(n):
    a[i] = int(input("Enter element"))

searchValue = int(input("enter the searchElement"))
index = searchElement(a, searchValue)

if index == -1:
    print "value" , searchValue , "not found"
else:
    print "value", searchValue ,"found at index:", index
