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
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self,data,k):
        pass

    def delete_node(self, x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
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
        element = int(input("Enter element to be inserted: "))
        checkElement = int(input("Enter element before which to insert: "))
        list.insert_before(data, x)
    elif option == 8:
        element = int(input("Enter element to be inserted: "))
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
    elif option == 19:
        break
    else:
        print "Incorrect option"
        break
