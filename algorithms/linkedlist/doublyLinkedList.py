class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def displayList(self):
        currentNode = self.head
        if self.head is None:
            print 'List is empty'
            return
        print 'List is: '
        while currentNode:
            print currentNode.data
            currentNode = currentNode.next

    def insertHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head.prev =newNode
        self.head = newNode

    def insertEnd(self, data):
        currentNode = self.head
        newNode = Node(data)
        if self.head is None:
            self.insertHead(data)
            return
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode


    def createList(self):
        n = int(input("Enter number of elements in the list: "))
        if n <= 0:
            print "Incorrect number of elements"
            return
        for i in range(n):
            data = int(input("Enter elements one by one: "))
            self.insertEnd(data)

    def insertAfter(self, data, x):
        newNode = Node(data)
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == x:
                break
            currentNode = currentNode.next
        if currentNode is None:
            print str(data) + ' not found in the list'
        else:
            newNode.prev = currentNode
            newNode.next = currentNode.next
            if currentNode.next is not None:
                currentNode.next.prev = newNode
            currentNode.next = newNode

    def insertBefore(self, data , x):
        newNode = Node(data)
        currentNode = self.head
        if self.head is None:
            print 'List is empty'
            return

        if self.head.data == data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return

        while currentNode:
            if currentNode.data == x:
                break
            currentNode = currentNode.next

        if currentNode is None:
            print str(data) + '  is not found in the list'
        else:
            newNode.next = currentNode
            newNode.prev = currentNode.prev
            currentNode.prev.next = newNode
            currentNode.prev = newNode

    def deleteFirstNode(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def deleteLastNode(self):
        if self.head is None:
            print 'List is empty'
            return

        if self.head.next is None:
            self.head = None
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.prev.next = None

    def reverseList(self):
        if self.head is None:
            return

        p1 = self.head
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev

        self.head = p1








list = DoublyLinkedList()
list.createList()


while True:
    print "1: Display List"
    print "2: Insert in empty list"
    print "3: Insert a node in the beginning of list"
    print "4: Insert a node at the end of the list"
    print "5: Insert a node after a specified node"
    print "6: Insert a node before a specified node"
    print "7: Delete first node"
    print "8: Delete last node"
    print "9: Delete any node"
    print "10: Reverse the list"
    print "11: Quit"


    option = int(input("Enter an option"))

    if option == 1:
        list.displayList()
    elif option == 2:
        element = int(input("Enter element to be inserted: "))
        list.insertEnd(element)
    elif option == 3:
        element = int(input("Enter element to be inserted: "))
        list.insertHead(element)

    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        list.insertEnd(element)
    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element after which to insert: "))
        list.insertAfter(element, checkElement)
    elif option == 6:
        data = int(input("Enter element to be inserted: "))
        x = int(input("Enter element before which to insert: "))
        list.insertBefore(data, x)

    elif option == 7:
        list.deleteFirstNode()
    elif option == 8:
        list.deleteLastNode()
    elif option == 9:
        element = int(input("Enter element to be deleted: "))
        list.deleteNode(element)
    elif option == 10:
        list.reverseList()
    elif option == 11:
        break
    else:
        print "Incorrect option"
        break
