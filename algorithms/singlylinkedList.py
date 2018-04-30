class Node (object):
    def __init__(self, data):
        self.data = data
        self.head = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList():
        currentNode = self.head
        if currentNode is None:
            print "List is empty"
        while True:
            if currentNode is None:
                break
            print currentNode
            currentNode = currentNode.next

    def listLength():
        length = 0
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            length+=1
        return length

    def searchElement(self, element):
        index = 0
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == element:
                return index
            index+=1
            currentNode = currentNode.next

        return "Element is not found"


    def insertHead(self, newNode):
        tempNode = newNode
        tempNode.next = self.head
        self.head= tempNode

    def insertEnd (self, newNode):
        if self.head is None:
            self.head = newNode
        lastNode = self.head
        while True:
            if lastNode.next is None:
                lastNode.next = newNode
                break
            lastNode = lastNode.next

    def createList(self):
        n = int(input("Enter the number of nodes:"))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the elements to be inserted"))
            self.insertEnd(data)
        
