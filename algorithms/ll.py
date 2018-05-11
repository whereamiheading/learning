class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def createList(self):
        n = int(input("Enter the number of nodes:  "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted:   "))
            self.insertEnd(data)

    def printList(self):
        if self.head is None:
            print "List is empty"
            return
        else:
            currentNode = self.head
            nodeCount = 0
            while currentNode is not None:
                print currentNode.data
                currentNode = currentNode.next
            print ""

    def listLength(self):
        currentNode = self.head
        nodeCount = 0
        while currentNode is not None:
            nodeCount +=1
            currentNode = currentNode.next
        print "Number of nodes in the list = " + str(nodeCount)

    def searchElement(self, element):
        currentNode = self.head
        position = 1
        while currentNode is not None:
            if currentNode.data == element:
                print str(element) + " is present at position: " + str(position)
                return True
            else:
                position +=1
                currentNode = currentNode.next
        else:
            print str(element) + " is not found in the list"
            return False

    def insertAfter(self,data,x):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == x:
                break
            currentNode = currentNode.next

        if currentNode is None:
            print str(x) + " is not present in the list "
        else:
            temp = Node(data)
            temp.next = currentNode.next
            currentNode.next = temp


    def insertBefore(self,data,x):
        if self.head is None:
            print "List is empty"
            return

        if x == self.head.data:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return

        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data ==x:
                break
            currentNode =currentNode.next

        if currentNode.next is None:
            print str(x) + " is not found in the list"
        else:
            temp = Node(data)
            temp.next = currentNode.next
            currentNode.next = temp

    def insertAt(self, data, position):
        if position == 1:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return

        currentNode =self.head
        currposition = 1

        while currposition < position -1 and currentNode is not None:
            currentNode = currentNode.next
            currposition +=1

        if currentNode is None:
            print "You can insert only upto position " + str(position)

        else:
            temp = Node(data)
            temp.next = currentNode.next
            currentNode.next = temp



    def insertHead(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insertEnd(self, data):
        lastNode = self.head
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        while lastNode.next is not None:
            lastNode =lastNode.next
        lastNode.next = temp


    def deleteFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteLastNode(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next

        previousNode.next = None


    def deleteNode(self, x):
        if self.head is None:
            print "list is empty"
            return

        if self.head.data == x:
            self.head = self.head.next
            return

        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == x:
                previousNode.next = currentNode.next
            previousNode = currentNode
            currentNode = currentNode.next

    def reverseList(self):
        currentNode = self.head
        prev = None
        while currentNode is not None:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev

    def bubbleSortExData(self):
        end = None
        while self.head != end:
            currentNode = self.head
            while currentNode.next != end:
                nextNode = currentNode.next
                if currentNode.data > nextNode.data:
                    currentNode.data , nextNode.data = nextNode.data, currentNode.data
                currentNode = currentNode.next
            end = currentNode



    def bubbleSortExLinks():
        pass
    def hasCycle (self):
        pass
    def insertCycle(self, x):
        pass
    def removeCycle(self):
        pass
    def findCycle(self):
        pass
    def merge2(self, list2):
        pass
    def __merge2(self, p1, p2):
        pass

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

    option = int(input("Enter an option:   "))

    if option == 1:
        list.printList()
    elif option == 2:
        list.listLength()
    elif option == 3:
        element = int(input("Enter element to be searched: "))
        list.searchElement(element)
    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        list.insertHead(element)
    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        list.insertEnd(element)
    elif option == 6:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element after which to insert: "))
        list.insertAt(element, checkElement)
    elif option == 7:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element before which to insert: "))
        list.insertBefore(element, checkElement)
    elif option == 8:
        element = int(input("Enter element to be inserted: "))
        position = int(input("Enter position at which to insert: "))
        list.insertAt(element,position)
    elif option == 9:
        list.deleteFirstNode()
    elif option == 10:
        list.deleteLastNode()
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
