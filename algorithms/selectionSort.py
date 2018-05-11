def selectionSort(list):
    for i in range (len(list)-1):
        print 'a ' + str(i)
        minIndex = i
        print 'b ' + str( minIndex)
        for j in range(i+1 , len(list)):
            print 'c '+ str(j)
            if list[j] < list[minIndex]:
                print 'd' + str(list[minIndex]), str(list[j])
                minIndex = j
                print 'e' +str(minIndex)
        print 'f ' + str(i)
        if i!= minIndex:
            print 'g'
            print list[i], list[minIndex]
            list[i], list[minIndex] = list[minIndex], list[i]
            print 'h ' +str(list[i])
    return list

list1 = [1,4,2,0]
#print selectionSort(list1)

def ss(lis):

    for i in range (len(lis) -1):
        minIndex = i
        for j in range (i+1, len(lis)):
            if lis[j] < lis[minIndex]:
                minIndex = j

        if i != minIndex:
            lis[i], lis[minIndex ] = lis[minIndex] , lis[i]
#ss(list1)

#print list1


def bb(lis):
    for x in range (len(lis) -1, 0, -1):
        print 'outer'
        print x
        for j in range (x):
            print 'inner'
            print j
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1] , lis[j]
                print lis[j], lis[j+1]
    return lis

print bb(list1)
