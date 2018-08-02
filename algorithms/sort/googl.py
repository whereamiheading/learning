#!/usr/bin/env python
## merge.py -- Merge two sorted lists -*- Python -*-
## Time-stamp: "2009-01-21 14:02:57 ghoseb"

l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]

def merge_sorted_lists1(l1, l2):
    """Merge sort two sorted lists

    Arguments:
    - `l1`: First sorted list
    - `l2`: Second sorted list
    """
    sorted_list = []

    # Copy both the args to make sure the original lists are not
    # modified
    l1 = l1[:]
    l2 = l2[:]

    while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
            sorted_list.append(item)
        else:
            item = l2.pop(0)
            sorted_list.append(item)

    # Add the remaining of the lists
    sorted_list.extend(l1 if l1 else l2)

    return sorted_list

def merge_sorted_lists2(l1, l2):
    sorted_list =[]
    l1 = l1[:]
    l2 = l2[:]
    while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
            sorted_list.append(item)
        else:
            item = l2.pop(0)
            sorted_list.append(item)

    # Add the remaining of the lists
    sorted_list.extend(l1 if l1 else l2)
    print 'within merge'
    print sorted_list
    print 'done with merge'
    return sorted_list

def merge_sorted_lists(l1, l2):
    """Merge sort two sorted lists

    Arguments:
    - `l1`: First sorted list
    - `l2`: Second sorted list
    """
    sorted_list = []

    # Copy both the args to make sure the original lists are not
    # modified
    l1 = l1[:]
    l2 = l2[:]

    while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
            sorted_list.append(item)
        else:
            item = l2.pop(0)
            sorted_list.append(item)

    # Add the remaining of the lists
    sorted_list.extend(l1 if l1 else l2)
    print 'within merge'
    print sorted_list
    print 'done with merge'
    return sorted_list

#
k1 = [0,3,5,6,9]
k2 =[11,1,2,8]
o=merge_sorted_lists1(k1, k2)
print o

if __name__ == '__main__':
    print merge_sorted_lists(l1, l2)
