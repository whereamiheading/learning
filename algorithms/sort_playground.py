def ss(l):
    for i in range(0, lean(l)-1):
        minIndex = i
        for j in range(i+1, len(l)):
            if l[j] < l[minIndex]:
                minIndex = j

        if i != minIndex:
            l[j], l[minIndex] = l[minIndex] , l[j]

    return l

def dd(l):
    for i in range (len(l)-1, 0 , -1):
        swaps = 0
        for j in range(i):
            if l[j] > len[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

            if swaps == 0:
                break
