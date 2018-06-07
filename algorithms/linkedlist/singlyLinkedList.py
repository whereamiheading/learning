class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print 'List is empty'
            return
        currentNode = self.head
        print 'List is : '
        while True:
            if currentNode is None:
                break
            print currentNode.data
            currentNode = currentNode.next

    def count_nodes(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count +=1
            currentNode = currentNode.next
        print "Number of elements: " + str(count)

    def search(self, x):
        currentPostition = 1
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == x:
                print str(x) + ' is at position ' + str(currentPostition)
                return True
            currentNode = currentNode.next
            currentPostition +=1
        else:
            print str(x) + ' is not found in list'
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


    def insert_at_end(self,data):
        lastNode = self.head
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = temp

    def create_list(self):
        n = int(input("Enter the number of elements to be inserted: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted:  "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == x:
                break
            currentNode = currentNode.next

        if currentNode is None:
            print '    ' + str(x) + ' is not present in the list'
        else:
            temp = Node(data)
            temp.next = currentNode.next
            currentNode.next = temp


    def insert_before(self, data, x):
        currentNode  = self.head
        if self.head is None:
            print ' list is empty'
            return

        if self.head.data == x:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return

        while currentNode is not None:
            if currentNode.next.data == x:
                break
            currentNode = currentNode.next

        if currentNode.next is None:
            print '    ' + str(x) + ' is not present in the list'
        else:
            temp = Node(data)
            temp.next = currentNode.next
            currentNode.next = temp




    def insert_at_position(self, data, position):
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
        # newNode = Node(data)
        # print self.count_nodes()
        # if newPosition <0 or newPosition > self.count_nodes():
        #     print 'list length error'
        #     return
        # currentPostition = 0
        # currentNode = self.head
        # if newPosition == 0:
        #     self.insert_in_beginning(newNode)
        #     return
        # while True:
        #     if currentPostition == newPosition:
        #         previousNode.next = newNode
        #         newNode.next = currentNode
        #         break
        #     previousNode = currentNode
        #     currentPostition +=1
        #     currentNode = currentNode.next



    def delete_node(self, x):
        if self.head is None:
            print 'List is empty'
            return

        if self.head.data == x:
            self.head = self.head.next
            return

        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data == x:
                break
            currentNode = currentNode.next

        if currentNode is None:
            print 'element not in list'
        else:
            currentNode.next = currentNode.next.next

    def delete_first_node(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            print ' list is empty'
            return

        if self.head.next is None:
            self.head = None
            return

        currentNode = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next
        currentNode.next = None



    def reverse_list(self):
        currentNode = self.head
        prev = None
        while currentNode :
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev


    def recur_reverse(self):

        def _recur_reverse(curr, prev ):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            _recur_reverse(curr, prev)
        self.head = _recur_reverse(curr = self.head, prev = None)



        # currentNode = self.head
        # prev = None
        # while currentNode is not None:
        #     next = currentNode.next
        #     currentNode.next = prev
        #     prev = currentNode
        #     currentNode = next
        # self.head = prev

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


list = SingleLinkedList()

list.create_list()

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
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        element = int(input("Enter element to be searched: "))
        list.search(element)
    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        list.insert_in_beginning(element)
    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        list.insert_at_end(element)
    elif option == 6:
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element after which to insert: "))
        list.insert_after(element, checkElement)
    elif option == 7:
        data = int(input("Enter element to be inserted: "))
        x7 = int(input("Enter element before which to insert: "))
        list.insert_before(data, x)
    elif option == 8:
        data = int(input("Enter element to be inserted: "))
        position = int(input("Enter position at which to insert: "))
        list.insert_at_position(data,position)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        element = int(input("Enter element to be deleted: "))
        list.delete_node(element)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.mergesort()
    elif option == 16:
        element = int(input("Enter element at which the cycle has to be inserted: "))
        list.insert_cycle(element)
    elif option == 17:
        if list.has_cycle():
            print "List has a cycle"
        else:
            print "List doesnt have a cycle"
    elif option == 18:
        list.remove_cycle()
    elif option == 20:
        list.recur_reverse()
    elif option == 19:
        break
    else:
        print "Incorrect option"
        break
