class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def createList(self):
        num = int(input("Enter the number of nodes"))
        if num == 0:
            return
        for i in range(num):
            newNode = int(input("Enter the element to be inserted"))
            self.insertEnd(newNode)

    def printList(self):
        currentNode = self.head
        if self.head is None:
            print "List is empty"
        else:
            while currentNode is not None:
                print currentNode.data
                currentNode = currentNode.next


    def listLength(self):
        currentNode = self.head
        length = 0
        while True:
            if currentNode is None:
                return length
            currentNode = currentNode.next
            length +=1
        return length

    def insertHead(self, data):
        currentNode = self.head
        newNode = Node(data)
        if self.head is None:
            currentNode = self.head
        else:
            newNode.next = currentNode
            self.head = newNode

    def insertEnd(self, data):
        temp = Node(data)
        if self.head is None:
            self.head =temp
            return
        lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next = temp

    def insertAt(self, data, position):
        currentNode = self.head
        currentPostition = 0
        if position == 0:
            self.insertHead(Node(data))
            return
        if position < 0 or position > self.listLength():
            print "Invalid position"
            return
        else:
            while True:
                if currentPostition == position:
                    previousNode.next = Node(data)
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

    def searchElement(self, element):
        currentNode = self.head
        currentPostition = 1

        while currentNode is not None:
            if currentNode.data == element:
                return currentPostition
            currentNode = currentNode.next
            currentPostition +=1

        else:
            print element, "not found in the list"
            return False





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

    option = int(input("Enter an option"))

    if option == 1:
        list.printList()
    elif option == 2:
        print list.listLength()
    elif option == 3:
        element = int(input("Enter element to be searched: "))
        print list.searchElement(element)
    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        list.insertHead(element)
    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        list.insertEnd(element)
    elif option == 6:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element after which to insert: "))
        list.insertAfterElement(element, checkElement)
    elif option == 7:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element before which to insert: "))
        list.insertBeforeElement(element)
    elif option == 8:
        element = int(input("Enter element to be inserted: "))
        position = int(input("Enter position at which to insert: "))
        list.insertAt(element,position)
    elif option == 9:
        list.deleteHead()
    elif option == 10:
        list.deleteEnd()
    elif option == 11:
        element = int(input("Enter element to be deleted: "))
        list.deleteNode(element)
    elif option == 12:
        list.reverseList()
    elif option == 13:
        list.bubbleSortExData()
    elif option == 14:
        list.bubbleSortExLinks()
    elif option == 15:
        list.mergeSort()
    elif option == 16:
        element = int(input("Enter element at which the cycle has to be inserted: "))
        list.insertCycle(element)
    elif option == 17:
        if list.hasCycle():
            print "List has a cycle"
        else:
            print "List doesnt have a cycle"
    elif option == 18:
        list.removeCycle()
    elif option == 19:
        break
    else:
        print "Incorrect option"
        break
