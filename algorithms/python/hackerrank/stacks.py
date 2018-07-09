## Stack Implementation
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

### We create an object and add numbers in a range using for loop. Once the stack is built, we try to extract each item from the stack until its empty-again using a for loop
### Un-comment the below block when required to test Stacks

# s = Stack()
# for i in range(4):
#     s.push(i)
#
# print s.isEmpty()
#
# for i in range(4):
#     print 'Taking out from stack:'
#     print s.pop()
# print s.isEmpty()


### Queue Implementation:

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enQueue(self, item):
        self.items.insert(0, item)

    def deQueue(self):
        #If reqd, uncomment below line to see the item being popped from queue
        #print self.items.pop()
        self.items.pop()

    def size(self):
        return len(self.items)
### We create an object and add numbers in a range using for loop. Once the queue is built, we try to extract each item from the queue until its empty-again using a for loop
### Un-comment the below block when required to test queue

# q=Queue()
# for i in range(4):
#     q.enQueue(i)
#
# print q.isEmpty()
#
# qlen = q.size()
#
# for i in range(qlen):
#     print q.deQueue()
#
# print q.isEmpty()




##Deque Implementation:

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def delFront(self):
        return self.items.pop()

    def delRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

### We create an object and add numbers from both the ends and also remove them from the dequeue.
### Un-comment the below block when required to test Deque
#
# d = Deque()
# d.addFront(4)
# d.addFront(3)
# size = d.size()
# print size
# d.addFront(5)
# d.addRear(2)
# size = d.size()
# print size
# print d.isEmpty()
#
# print str(d.delFront()) + ' ' + str(d.delRear())

# st = 'This is to <test (how {parenthesis} work)>'
#st = "This is to <test (how '{'parenthesis)'}' work)>"
st = '({[}]})'
def balance(st):
    dt = {
    '<':'>',
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
    }
    stack =[]
    #stack = [<,(,{]
    for letter in st:
        if letter in dt:
            stack.append(letter)
        else:
            if letter in dt.values():
                close = stack.pop()
                # letter = } , close = {
                if dt[close] == letter:
                    pass
                else:
                    return False
    return True

# print balance(st)

st1 = "this is < as {good }() as it can '{'get'}')>"
def balance1(st):
    dt = {  '{':'}',
            '(':')',
            '[':']',
            '<':'>' }
    stack = []
    for letter in st1:
        if letter in dt:
            stack.append(letter)
            if len(stack) ==0:
                return False
        else:
            if letter in dt.values():
                open_bracket = stack.pop()
                #letter = } and open_bracket = {
                if dt[open_bracket] != letter:
                    return False
                #     pass
                # else:
                #     return False
    return True

print balance1(st1)



## Implement a Queue using two stacks:

class Queue4mStack(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)
        print self.instack

    def dequeue(self):
        print '77777'
        if not self.outstack:
            while self.instack:
                # print '^^&^&^'
                self.outstack.append(self.instack.pop())

        #print self.outstack.pop()
        return self.outstack.pop()

    def size(self):
        return len(self.outstack)

q4s = Queue4mStack()
for i in range(4):
    q4s.enqueue(i)

print q4s.size()
for i in range(4):
    q4s.dequeue()
print 'final size:'
print q4s.size()
