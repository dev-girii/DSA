class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None

class Dll:
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
        newData.prev = curr 
    
    def print(self):
        if not self.head:
            print("There are no data to print")
            return 
        curr = self.head 
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next 
a = Dll()        
a.append(10)
a.append(30)
a.append(20)
a.print()