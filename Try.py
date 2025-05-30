class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Sll:
    def __init__(self):
        self.head = None 
    
    def appendData(self,data):
        newData = Node(data)
        if self.head is None:
            self.head = newData 
            return 
        curr = self.head 
        while curr.next:
            curr = curr.next 
        curr.next = newData
    
    def printData(self):
        print("\n")
        curr = self.head 
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next 

    def deleteAtLast(self):
        if not self.head:
            print("No data to delete")
        
        if not self.head.next:
            self.head = None 
            print("Deleted")
        
        curr = self.head 
        prev = None 
        while curr.next.next:
            prev = curr 
            curr = curr.next 
        prev.next  = curr 
        curr.next = None 

    def insertAtFirst(self,data):
        newData = Node(data)
        if not self.head:
            self.head = newData 
            return 
        curr = self.head 
        self.head = newData 
        self.head.next = curr 

    def search(self,data):
        if not self.head:
            print("\nNo element to search")
            return
        
        if not self.head.next:
            if self.head.data == data:
                print("\nFound at Index: 0")
        index = 0
        curr = self.head 
        while curr:
            if curr.data == data:
                print("\nFound at index: ", index)
                return 
            index += 1
            curr = curr.next 
        else:
            print(f"\n{data} Not found")
a = Sll()
a.search(2)
a.appendData(1)
a.appendData(2)
a.appendData(3)
a.appendData(4)
a.printData()
a.search(20)
a.insertAtFirst(20)
a.deleteAtLast()
a.printData()
a.deleteAtLast()
a.printData()