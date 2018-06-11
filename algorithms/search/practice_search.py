def linearSearch(array, searchValue):
	for i in range(len(array)):
		if array[i] == searchValue:
			return i
		
	return -1


def binarySearch(array, searchValue):
	first = 0
	last = len(array) - 1
	print 'Now we are in binarySearch: '
	while first <= last:
		mid = (first+last)//2
		if searchValue < array[mid]:
			last = mid -1
		elif searchValue > array[mid]:
			first = mid +1
		else:
			return mid

	else:
		return -1



num = int(input('Enter the number of elements in the array:  '))
arr = [None]*num
print 'array lenght is : ' + str(len(arr))
for i in range(num):
	arr[i] = int(input("Enter element one at a time: "))

searchValue = int(input("Enter element to be searched: "))

index = linearSearch(arr, searchValue)


if index == -1:
	print str(searchValue) + ' is not present in the list'

else:
	print str(searchValue) + ' is present at index using linearSearch : ' + str(index)

b_index = binarySearch(arr, searchValue)

if b_index == -1:
	print str(searchValue) + ' is not present in the list'

else:
	print str(searchValue) + ' is present at index using binarySearch: ' + str(b_index)


