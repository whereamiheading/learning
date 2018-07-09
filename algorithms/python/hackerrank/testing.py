# def solve(s, d, m):
#     num = 0
#     for i in range(len(s)):
#         inter = s[i:i+m]
#         if len(inter) == m and sum(inter) == d :
#              print inter
#              num +=1
#     return num
#
#
# s=[1, 2 ,1, 2, 3]
# d = 3
# m =2
# result = solve(s, d, m)

###length of longestsubstring
def lengthOfLongestSubstring(s):
        longest = []
        max_length = 0

        for c in s:
            if c in longest:
                max_length = max(max_length, len(longest))
                longest = longest[longest.index(c)+1:]
            longest.append(c)

        max_length = max(max_length, len(longest))
        return max_length



res= lengthOfLongestSubstring('abcabcd')
print res


### check the meeting calendar intersection. Re-order and then club them together

def calen(meetings):
    sorted_meetings = sorted(meetings)
    merged_list = [sorted_meetings[0]]

    for curr_start, curr_end in sorted_meetings[1:]:
        last_start, last_end = merged_list[-1]

        if curr_start <= last_end:
            merged_list[-1] = (last_start, max(last_end, curr_end))
        else:
            merged_list.append((curr_start, curr_end))
    return merged_list

meetings =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

print 'Clubbing meeting calendars/tuples'
output = calen(meetings)
print output

### reverse characters in string:

def reverse_string (s):
    s_list = []
    for i in s:
        s_list.append(i)
    for i in range(len(s_list)/2):
        s_list[i], s_list[len(s) -i -1 ] =  s_list[len(s) -i -1 ], s_list[i]
    return ''.join(s_list)

print 'Reversing a string'
output = reverse_string('abcd')
print output


### reverse characters in string:

def reverse_list (s_list):
    for i in range(len(s_list)/2):
        s_list[i], s_list[len(s_list) -i -1 ] =  s_list[len(s_list) -i -1 ], s_list[i]
    print s_list
    new_string = ''.join(s_list)
    op = []
    for i in new_string.split():
        op.append(reverse_string(i))
    return ' '.join(op)

print 'Reversing a list'
output = reverse_list([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ])
print output



### Merging two sorted input lists

def merge(list1, list2):
    # list1 = [1,3,6,7]
    # list2 = [2,4,5,8]
    if not list1: return list2
    if not list2: return list1
    sorted_list = []
    while (list1 and list2):
        if (list1[0] <= list2 [0]):
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))

    sorted_list.extend(list1 if list1 else list2)
    return sorted_list

output = merge([2,3,6,7] ,[2,4,5,8, 9] )
print output



### check permutations of palindrome in a string:
def perm_palin(string):
    seen_set = set ()

    for char in string:
        if char in seen_set:
            seen_set.remove(char)
        else:
            seen_set.add(char)

    return len(seen_set)<=1

output = perm_palin('civvic')
print output


#
# def has_palindrome_permutation(the_string):
# # Track characters we've seen an odd number of times
#     unpaired_characters = set()
#
#     for char in the_string:
#         if char in unpaired_characters:
#             unpaired_characters.remove(char)
#         else:
#             unpaired_characters.add(char)
#
#     # The string has a palindrome permutation if it
#     # has one or zero characters without a pair
#     return len(unpaired_characters) <= 1
#
# output = has_palindrome_permutation('civvic')
# print output

## Bubble sort
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr
output= bubble_sort([4,3,5, 1, 7, 9, 2,0])
print output


##Selection Sort
def selection_sort(arr):
    for i in range(len(arr) -1 ):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]: ## < -- ascending , > --- descending
                minIndex = j
        if minIndex != i:
            arr[i] , arr[minIndex] = arr[minIndex] , arr[i]
    return  arr
output = selection_sort([2,1,4,0,9,5])
print output
