def linearSearch (arr, find):
    for i in range(len(arr)):
        if arr[i] == find:
            return i

    return -1

num = int(input("Enter the elements in the array"))
arr = [None]*num
print 'Enter the elements'
for i in range(num):
    arr[i] =  int(input("Enter the element: "))

find = int(input("Enter the element to be searched"))

index = linearSearch(arr, find)

if index == -1:
    print "Element " + str(find) + " not present in list"

else:
    print "element " + str(find) + " present at index " + str(index)
