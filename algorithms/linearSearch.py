def searchElement(a, searchValue):
    for i in range(len(a)):
        if a[i] == searchValue:
            return i

    return -1



n = int(input("Enter the num of elements"))
print "enter elements"
a =[None]*n
for i in range(n):
    a[i] = int(input("Enter element"))

searchValue = int(input("enter the searchElement"))
index = searchElement(a,searchValue)

if index == -1:
    print "value" , searchValue , "not found"
else:
    print "value", searchValue ,"found at index:", index
