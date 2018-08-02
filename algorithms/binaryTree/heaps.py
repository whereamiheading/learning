class Heap:
    def __init__(self, maxsize =100):
        self.a =[None]*maxsize
        self.n = 0
        self.a[0] = 9999999

    def insert(self, value):
        self.n +=1
        self.a[self.n] = value
        self.restore_up(self.n)

    def restore_up(self, i):
        k = self.a[i]
        iparent = i//2

        while self.a[iparent] < k:  ## Compare parent value with kth element value. If parent is les than k, then push parent to i-th location and then put k in parent s place
            self.a[i] =self.a[iparent]
            i = iparent
            iparent = i//2
        self.a[i] =k

    def delete_root(self):
        if self.n ==0:
            raise HeapEmptyError("Heap is empty")

        maxValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -=1
        self.restore_down(1)
        return maxValue

    def restore_down(self, i):
        k = self.a[i]
        lchild = 2*i
        rchild = 2*i+1

        while rchild <= self.n:
            if k >=self.a[lchild] and k >= self.a[rchild]:
                self.a[i] =k
                return
            else:
                if self.a[lchild] > self.a[rchild]:
                    self.a[i]  = self.a[lchild]
                    i = lchild
                else:
                    self.a[i] = self.a[rchild]
                    i = rchild

            lchild = 2*i
            rchild = 2*i+1

        if lchild == self.n and k < self.a[lchild]:
            self.a[i] = self.a[lchild]
            i = lchild
        self.a[i] =k




    def display(self):
        if self.n == 0:
            print 'Heap is empty'
            return

        print 'heap size: ' + str(self.n)
        for i in range(1, self.n+1):
            print self.a[i]


h = Heap(20)
while True:
    print '1: Insert'
    print '2: Delete'
    print '3: Display'
    print '4: Exit'
    print 'Enter ur choice: '
    choice = int(input("Enter ur choice: "))

    if choice ==1:
        value = int(input("enter thevalue to be inserted : "))
        h.insert(value)
    elif choice ==2:
        print "Maximum value of heap is: " +str(h.delete_root())
    elif choice ==3:
        h.display()
    elif choice ==4:
        break
    else:
        print 'Wrong choice'
