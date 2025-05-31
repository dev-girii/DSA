class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 


def hascycle(head):
    slow = fast = head 
    while fast!=None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            # return true     Just to check if it has cycle
            slow = head 
            while slow!=fast:                # To return the node at which the cycle starts
                slow = slow.next 
                fast = fast.next 
            return slow.data
    else:
        return False 
        
a = Node(3)        
b = Node(4)
c = Node(5)
d = Node(6) 

a.next = b 
b.next = c
c.next = d 
d.next = b 

print(hascycle(a))
