class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isListempty(self):
        if self.head is None:
            return True
        else:
            return False

    def addElement(self, newNode):
        currentNode = self.head
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        if self.head is None:
            print 'List is empty'
        else:
            while True:
                if currentNode is None:
                    break
                print currentNode.data
                currentNode = currentNode.next


    def insertHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def listLength(self):
        currentNode= self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next

        return length


    def insertAt(self, newNode, newPosition):
        print self.listLength()
        if newPosition <0 or newPosition > self.listLength():
            print 'list length error'
            return
        currentPostition = 0
        currentNode = self.head
        if newPosition == 0:
            self.insertHead(newNode)
            return
        while True:
            if currentPostition == newPosition:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentPostition +=1
            currentNode = currentNode.next


    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None



    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print 'invalid position'
            return
        if isListempty is False:
            currentNode = self.head
            currentPostition = 0
            while True:
                if currentPostition == position:
                    previousNode.next = currentNode.next
                    currentNode.next  = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPostition = +1





# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def addElement(self,newNode):
#         currentNode = self.head
#         if self.head is None:
#             self.head = newNode
#         else:
#             lastNode = self.head
#             while True:
#                 if lastNode.next is None:
#                     break
#                 lastNode = lastNode.next
#
#             lastNode.next = newNode
#
#     def printList(self):
#         if self.head is None:
#             print ' List is empty'
#             return
#         currentNode = self.head
#         while True:
#             if currentNode is None:
#                 break
#             print currentNode.data
#             currentNode = currentNode.next
#
#
#

#
f_node = Node("John")
s_node = Node("Meyer")
t_node = Node("Michelle")
#
ll = LinkedList()
ll.addElement(f_node)
ll.addElement(s_node)
ll.insertHead(t_node)
#ll.insertAt(t_node, 3)
ll.deleteEnd()
ll.printList()
