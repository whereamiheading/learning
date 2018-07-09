1. Apple and oranges:

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    A = 0
    B = 0
    for i in range(len(apples)):
        if apples[i]>= (s-a) and apples[i] <= (t-a):
            A+=1
        else:
            pass
    for j in range(len(oranges)):
        if oranges[j] < 0 and abs( oranges[j]) >= (b-t) and abs(oranges[j]) <= (b-s):
            B +=1
        else:
            pass

    print str(A) + '\n' + str(B)


if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)




2.  birthday chocolate:

def solve(s, d, m):
    num = 0
    for i in range(len(s)):
        inter = s[i:i+m]
        if len(inter) == m and sum(inter) == d :
             print inter
             num +=1
    return num

3. birds

#!/bin/python

import sys


n = int(raw_input().strip())
l =list( map(int, raw_input().strip().split(' ')))
l.sort()
ans=l[0]
count=1
max=1
for i in range(1,n):
    if l[i]==l[i-1]:
        count+=1
    else:
        count=1
    if count>max:
        max=count
        ans=l[i]
print ans


3. longest substring:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        new_list = []
        for letter in s:
            if letter in new_list:
                max_len = max(max_len, len(new_list))
                new_list = new_list[new_list.index(letter)+1:]
            new_list.append(letter)

        max_len = max(max_len, len(new_list))
        return max_len

5. most common word:

def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        """
        O(paragraph) Time
        O(paragraph+banned) Space
        """

        banned = set(banned)
        # maintain dict of word frequency of words which are not in banned
        hashmap = {}
        mostcommon = ''
        count = 0
        for word in paragraph.split():
            word = word.strip('!?\',;.').lower()
            # while inserting words in frequency keep track of most frequent word
            if word not in banned:
                hashmap[word] = hashmap.get(word,0) + 1
                if hashmap[word] > count:
                    count = hashmap[word]
                    mostcommon = word
        return mostcommon


6. goat latin:
class Solution(object):
    def toGoatLatin(self, S):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        return ' '.join([
            (token + 'ma' if token[0] in vowels else token[1:] + token[0] + 'ma') + 'a'*(i+1)
            for i, token in enumerate(S.split(' '))
        ])

7. jewels & stone:
for stone in S;
    if stone in J:
        count+=1
return count

8. subdomains count:


def subdomains (self, subdomains ):
    from collections import defaultdict
    domain_visits = defaultdict(int)

    for cp_domain in subdomains:
        num_visits, domain = int(cp.domain.split(' '))

        split_domain = domain.split('.')
        for i in range(len(split_domain)):
            sub_domain = '.'.join(split_domain[i:])
            domain_visits[sub_domain] = domain_visits[sub_domain] + num_visits
    return [ str(v) + ' ' + k    for k,v in domain_visits.items()]


6. keyborad row:

def words:

    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    res = []
    for word in words:
        for row in keyboard:
            if set(word.lower()).issubset(row):
                res.append(word)
    return res


7.
### InterviewCake
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

output = calen(meetings)
print output

8.
### InterviewCake
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


9. ##InterviewCake
## reverse words and their characters in a list:

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



##InterviewCake
### Merging two sorted input lists

def merge(list1, list2):
    # list1 = [1,3,6,7]
    # list2 = [2,4,5,8]
    #check if lists are empty
    if not list1: return list2
    if not list2: return list1
    sorted_list = []
    while (list1 and list2): #while there are elements in both the lists
        if (list1[0] <= list2 [0]):
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))

    sorted_list.extend(list1 if list1 else list2) # extend with the larger list left over elements
    return sorted_list

output = merge([2,3,6,7] ,[2,4,5,8, 9] )
print output


##InterviewCake
### To get two movies which would fit the flight length

def can_two_movies_fill_flight(movie_lengths, flight_length):
# Movie lengths we've seen so far
movie_lengths_seen = set()

for first_movie_length in movie_lengths:
    matching_second_movie_length = flight_length - first_movie_length
    if matching_second_movie_length in movie_lengths_seen:
        return True
    movie_lengths_seen.add(first_movie_length)

# We never found a match, so return False
return False


##InterviewCake
## see if a permutation of string is palindrome or not
def perm_palin(string):
    seen_set = set ()

    for char in string:
        if char in seen_set:
            seen_set.remove(char)
        else:
            seen_set.add(char)

    return len(seen_set)<=1


## nth to LastNode - Jose Portilla

def nth_to_last(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):

        if not right_pointer.next:
            raise LookUpError("Error: n is larger than the list")
        right_pointer = right_pointer.next

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer



# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in xrange(0, len(str)/2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
