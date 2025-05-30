# Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head 
        while curr.next:
            curr = curr.next 
        curr.next = new_node 

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def deleteNode(self,key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None 
            return 
        
        prev = None 
        while current and current.data != key:
            prev = current
            current = current.next 

        if current is None:
            return 
        
        prev.next = current.next 
        current = None

l1 = SingleLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)     
l1.deleteNode(10)   
l1.display()

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        new_node = DoubleNode(data)
        new_node.next = self.head 
        if self.head is not None:
            self.head.prev = new_node 
        self.head = new_node 