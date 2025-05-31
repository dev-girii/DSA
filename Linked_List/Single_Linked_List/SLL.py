class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Sll:
    def __init__(self):
        self.head = None 
    
    def append(self,data):
        newData = Node(data) 
        if not self.head:
            self.head = newData
            return 
        curr = self.head 
        while curr.next:
            curr = curr.next 
        curr.next = newData 
    
    def print(self):
        if not self.head:
            print("No data to display")
            return 
        curr = self.head  
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next 
    
    def search(self, data):
        if not self.head:
            print("No data to search")
            return 
        if not self.head.next:
            if self.head == data:
                print("Found at index 0")
                return 
        index = 0
        curr = self.head 
        while curr:
            if curr.data == data:
                print(f"Found at index: {index}")
            index +=1
            curr = curr.next 

    def deleteAtLast(self):
        if not self.head:
            print("Nothing to delete")
            return 
        if not self.head.next:
            self.head = None 
            return 
        curr = self.head 
        while curr.next.next:
            print(curr.data)
            curr = curr.next 
        curr.next = None 
a = Sll()
a.append(10)
a.append(20)
a.append(30)
a.print()
a.search(30)
a.deleteAtLast()
a.print()