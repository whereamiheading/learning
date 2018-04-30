class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def createList():
        self.head = None

    def printList():
        currentNode = self.head
        if self.head is None:
            print "List is empty"
        else:
            print currentNode
            currentNode = currentNode.next

    def insertHead(self, newNode):
        currentNode = self.head
        if self.head is None:
            currentNode = self.head
        else:
            newNode.next = currentNode
            self.head = newNode

    def listLength():
        currentNode = self.head
        length = 0
        while True:
            if currentNode is None:
                return length
            currentNode = currentNode.next
            length +=1


    def insertEnd(self, newNode):
        lastNode = self.head
        if self.head is None:
            self.head = newNode
        else:
            while True:
                if lastNode.next is None:
                    lastNode.next = newNode
                    break
                lastNode = lastNode.next

    def insertAt(self, newNode, position):
        currentNode = self.head
        currentPostition = 0
        if position == 0:
            self.insertHead(newNode)
            return
        if position < 0 or position > self.listLength():
            print "Invalid position"
            return
        else:
            while True:
                if currentPostition == position:
                    previousNode.next = newNode
                    newNode.next = currentNode
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPostition +=1

    def deleteHead():
        currentNode = self.head
        self.head = currentNode.next

    def deleteEnd():
        lastNode = self.head
        while True:
            if lastNode.next is None:
                previousNode.next = None
                break
            previousNode = lastNode
            lastNode = lastNode.next

    def deleteAt(self, position):
        currentNode = self.head
        currentPostition = 0
        while True:
            if currentNode == position:
                previousNode.next = currentNode.next
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPostition +=1

    def serachElement(self, element):
        currentNode = self.head
        currentPostition = 0

        while currentNode is not None:
            if currentNode.data == element:
                return currentPostition
            currentNode = currentNode.next
            currentPostition +=1





list = LinkedList()

list.createList()

while True:
    print "1: Display List"
    print "2: Count the num of nodes"
    print "3: Search for an element"
    print "4: Insert in empty list/insert in the beginning of list"
    print "5: Insert a node at the end of the list"
    print "6: Insert a node after a specified node"
    print "7: Insert a node before a specified node"
    print "8. Insert a node at a given position"
    print "9: Delete first node"
    print "10: Delete last node"
    print "11: Delete any node"
    print "12: Reverse the list"
    print "13: Bubble sort by changing data"
    print "14: Bubble sort by changing links"
    print "15: Mergesort"
    print "16: Insert cycle"
    print "17: Detect cycle"
    print "18: Remove cycle"
    print "19: Quit"

option = int(input("Enter an option")):

if option == 1:
    list.printList()
elif option == 2:
    list.listLength()
elif option == 3:
    element = int(input("Enter element to be searched: "))
    list.searchElement(element)
