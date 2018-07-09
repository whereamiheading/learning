###compress of strins:
from collections import defaultdict
def compress(string):
    r = ''
    cnt = 1
    length = len(string)
    i=1

    while i < length:

        if string[i] == string[i-1]:
            cnt +=1
        else:
            r = r + string[i-1] + str(cnt)
            cnt =1
        i+=1
    r = r + string[i-1] + str(cnt)
    return r

res = compress("AAb")
print res

##uniqueness:

def uniq(string):
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            characters.add(letter)

    return True

res= uniq('abcd')
print res
res = uniq('abcdea')
print res

####reverse:

s ='   hello how are you mister   '
lst = s.split(' ')
l =[]
for element in lst:
    if element == '':
        pass
    else:
        l.append(element)
print len(l)
print len(l)/2
print '******'

for i in range(len(l)/2):
    print l[i] + '---'
    print l[len(l)-i-1] + '++++'
    l[i], l[len(l)-i-1] = l[len(l)-i-1][::-1], l[i][::-1]

print ' '.join(l)


####anagram:

def anagram(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    dt = {}

    if len(s1) != len(s2):
        return False

    for letter in s1:
        if letter in dt:
            dt[letter] +=1
        else:
            dt[letter] =1

    for letter in s2:
        if letter in dt:
            dt[letter] -= 1
        else:
            dt[letter] =1

    for k in dt:
        if dt[k] != 0:
            return False

    return True

s = anagram('het' , 'tah')
print s


##pair sum:

def pair_sum(arr , k):
    seen = set ()
    output = set ()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add(( min(num, target), max(num, target)))
    return output

res = pair_sum([1,2,3,2] , 4)
print res



## missing number from second array:

def finder1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

arr1 = [2,3,4,5,1]
arr2 = [2,3,5,1]
res = finder1(arr1, arr2)
print res


def finder2(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        if num in d:
            d[num] +=1
        else:
            d[num] =1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1

arr1 = [2,3,4,5,1]
arr2 = [2,3,5,1]
res = finder2(arr1, arr2)
print res


def reverse_string(arr):
    lst = []
    for element in arr:
        lst.append(element)
    for i in range(len(lst)/2):
        lst[i], lst[len(lst) - i-1] = lst[len(lst) - i-1], lst[i]

    return lst
res= reverse_string('abcd')
res = ''.join(res)
print res



def singleelement(arr):
    d = defaultdict(int)
    for el in arr:
        if el in d:
            d[el] +=1
        else:
            d[el] = 1
    for key in d:
        if d[key] == 1:
            return key

    return None

res = singleelement([3,2,3,1,1])
print res



def max1(arr):
    max_count = 0
    running_cnt = 0
    for el in arr:
        if el ==1:
            running_cnt +=1
        elif el ==0 :
            max_count =max(running_cnt,max_count)
            running_cnt = 0
    return max(running_cnt,max_count)

res = max1([1,1,1,1,0,1,1,1,1,1])
print res



l = [64, 25, 12, 22, 11, 1,2,44,3,-122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print l


##group anagrams:


tally = {}

for key, word in [(''.join(sorted(word)), word) for word in strs]: ## aet: tea aet: eat
	if key in tally:
		tally[key].append(word)
	else:
		tally[key] = [word]

return list(tally.values())
