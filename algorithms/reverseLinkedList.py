class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

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



    def reverseList(self):
        currentNode = self.head
        prev = None
        while currentNode is not None:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next

        self.head = prev

fNode = Node(1)
sNode = Node(2)
tNode = Node(3)
list = LinkedList()
list.insertEnd(fNode)
list.insertEnd(sNode)
list.insertEnd(tNode)

print list.printList()
print list.reverseList()
