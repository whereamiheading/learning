class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0

        while currentNode is not None:
            length +=1
            currentNode = currentNode.next

        return length

    def insertEnd(self, newNode):
        if self.head is None:
            self.head =newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print "List is empty"
            return
        currentNode = self.head

        while True:
            if currentNode is None:
                break
            print currentNode.data
            currentNode = currentNode.next


    def insertHead(self,newestNode):

        tempNode = self.head
        newestNode.next = tempNode
        self.head= newestNode
        del tempNode

    def insertAt(self, newNode , position):

        if position <0 or position > self.listLength():
            print "Invalid List Length"
            return

        if position == 0:
            self.insertHead(newNode)
            return

        currentNode = self.head
        currentpostition = 0
        while True:
            if currentpostition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentpostition +=1

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def deleteAt(self, position):
        currentPostition = 0
        currentNode = self.head
        while True:
            if currentNode.next is None:
                self.deleteEnd()
                break
            if currentPostition == position:
                previousNode.next = currentNode.next
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPostition +=1



firstNode = Node("Sridhar")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Gurram")
linkedList.insertEnd(secondNode)
thirdNode = Node("Murthy")
linkedList.insertEnd(thirdNode)

fourthNode = Node("Hello")
linkedList.insertHead(fourthNode)
addressNode = Node ("Mr.")
linkedList.insertAt(addressNode, -1)
#linkedList.deleteEnd()
#linkedList.printList()
linkedList.deleteAt(1)
linkedList.printList()
