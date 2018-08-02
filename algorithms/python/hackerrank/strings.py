#superReducedString

def super_reduced_string(s):
    res = []
    for c in s:
        if res and res[-1] == c:  # If list is non empty and last list element  == input char
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or "Empty String"

print super_reduced_string('aabccdaa')
print '*******'


# import sys
#
# s = input().strip()
# n=1
# for l in s:
#     if l.isupper():
#         n+=1
# print (n)
def camelcase(s):
    n=1
    for char in s:
        if char == char.upper():
            n+=1
    return n

print camelcase('saveAsTextFile')
print '*******'


import re
#n=int(input())
#password=input()
def printPassword(n, password):
    count=0
    if re.search(r'\d',password):
        count+=1
    if re.search(r'[a-z]',password):
        count+=1
    if re.search(r'[A-Z]',password):
        count+=1
    if re.search(r'[\!\@\#\$\%\^\&\*\(\)\-\+]',password):
        count+=1
    print n, count
    print(max(6-n,4-count))

printPassword(10, 'A1nY#haner')
