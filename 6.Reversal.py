class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:   
            self.head = new_node
            return
        last = self.head
        while last.next:    
            last = last.next
        last.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

l1 = Linkedlist()
l1.append(1)
l1.append(2)
l1.append(3)
l1.print_list()
l1.reverse()
l1.print_list()
