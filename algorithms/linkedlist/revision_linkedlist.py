class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:

    def __init__(self):
        self.head = None

	def displayList(self):
		if self.head is None:
			print 'List is empty'
			return
		lastNode = self.head

		while lastNode:
			print lastNode.data
			lastNode = lastNode.next


    def listLength(self):
        if self.head == None:
            print 'List is empty'
            return
        count = 0
        currentNode = self.head
        while currentNode:
            count +=1
            currentNode = currentNode.next
        return count

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode



    def insertHead(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode
        return

	def createList(self):
		num = int(input("Enter number of elements in the list: "))
		for i in range(num):
			data = int(input("Enter elements to be inserted into the list: "))
			self.insertEnd(data)

	def insertAfter(self, data ,x):
		newNode = Node(data)
        currentNode = self.head

        while currentNode:
            if currentNode.data == x:
                newNode.next = currentNode.next
                currentNode.next = newNode
        else:
            print str(x) + ' is not present in the list'


	def insertBefore(self, data, x):
		newNode = Node(data)
        if self.head.data == x:
            newNode.next = self.head
            self.head = newNode
            return

        currentNode = self.head

        while currentNode:
            if currentNode.data ==x:
                newNode.next = previousNode.next
                previousNode.next = newNode
                return
            previousNode = currentNode
            currentNode = currentNode.next

        else:
            print str(x) + ' is not present in the list'

	def insertAt(self, data, position):
		newNode = Node(data)
        currentPostition = 1
        listLen = self.listLength()
        currentNode = self.head

        if position < 0 or position > listLen:
            print 'Incorrect length'
            return

        if position == 1:
            newNode.next = self.head
            self.head = newNode
            return

        while currentNode:
            if currentPosition == position:
                newNode.next = previousNode.next
                previousNode.next = newNode
                return
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1




    def deleteFirstNode(self):
        if self.head.next is None:
            self.head = None
            return

        self.head= self.head.next

	def deleteLastNode(self):
		currentNode = self.head

        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        previosNode.next = None


	def deleteNode(self, data):
		currentNode = self.head
		if self.listLength == 0 :
			self.head = None
			return

		currentNode = self.head
		if currentNode.data == data:
			self.head = currentNode.next
			return

        while currentNode:
            if currentNode.data == data:
                previosNode.next = currentNode.next
            previosNode = currentNode
            currentNode = currentNode.next

	def reverseList(self):
		prev = None
        currentNode = self.head
        while currentNode:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev

	def recur_reverse(self):

		def _recur_reverse(curr, prev):
			pass




    def bubble_sort_exdata1(self):

        end = None
        while self.head.next != end:
            fn = self.head
            while fn.next != end :
                sn = fn.next
                if fn.data > sn.data:
                    fn.data, sn.data = sn.data, fn.data
                fn = fn.next
            end = fn




	def bubble_sort_exdata2(self):
		pass

	def bubble_sort_exdata(self):
		pass


	def bubble_sort_exlinks(self):
	    pass

	def has_cycle(self):
	    pass

	def find_cycle(self):
	    pass

	def remove_cycle(self):
	    pass

	def insert_cycle(self):
	    pass

	def merge2(self,list2):
	    pass

	def _merge(self, p1, p2):
	    pass

	def merge_sort(self):
	    pass

	def _merge_sort_rec(self, listStart):
	    pass

	def _divide_list(self,p):
	    pass

list = singlyLinkedList()

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
    print "20: Recur reverse cycle"

    option = int(input("Enter an option"))

    if option == 1:
        list.displayList()
    elif option == 2:
        list_length = list.listlength()
        print 'List length is : ' + str(list_length)
    elif option == 3:
        element = int(input("Enter element to be searched: "))
        list.search(element)
    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        list.insertHead(element)
    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        list.insertEnd(element)
    elif option == 6:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element after which to insert: "))
        list.insertAfter(element, checkElement)
    elif option == 7:
        data = int(input("Enter element to be inserted: "))
        x = int(input("Enter element before which to insert: "))
        list.insertBefore(data, x)
    elif option == 8:
        data = int(input("Enter element to be inserted: "))
        position = int(input("Enter position at which to insert: "))
        list.insertAt(data,position)
    elif option == 9:
        list.deleteFirstNode()
    elif option == 10:
        list.deleteLastNode()
    elif option == 11:
        element = int(input("Enter element to be deleted: "))
        list.deleteNode(element)
    elif option == 12:
        list.reverseList()
    elif option == 20:
    	list.recur_reverse()
    elif option == 13:
    	list.bubble_sort_exdata()
    # elif option == 14:
    #     list.bubble_sort_exlinks()
    # elif option == 15:
    #     list.mergesort()
    # elif option == 16:
    #     element = int(input("Enter element at which the cycle has to be inserted: "))
    #     list.insert_cycle(element)
    # elif option == 17:
    #     if list.has_cycle():
    #         print "List has a cycle"
    #     else:
    #         print "List doesnt have a cycle"
    # elif option == 18:
    #     list.remove_cycle()

	#elif option == 20:
	#	pass
		#list.recur_reverse()
    elif option == 19:
        break
    else:
        print "Incorrect option"
        break
