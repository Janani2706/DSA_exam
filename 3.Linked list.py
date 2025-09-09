class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head=newnode
    def append(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        second = self.head
        while second.next:
            second = second.next
        second.next=newnode
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="\n")
            current = current.next
        print("none")
l1=linked()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.print_list()