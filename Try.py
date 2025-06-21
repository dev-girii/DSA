# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None 

# class Sll:
#     def __init__(self):
#         self.head = None 
    
#     def appendData(self,data):
#         newData = Node(data)
#         if self.head is None:
#             self.head = newData 
#             return 
#         curr = self.head 
#         while curr.next:
#             curr = curr.next 
#         curr.next = newData
    
#     def printData(self):
#         print("\n")
#         curr = self.head 
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next 

#     def deleteAtLast(self):
#         if not self.head:
#             print("No data to delete")
        
#         if not self.head.next:
#             self.head = None 
#             print("Deleted")
        
#         curr = self.head 
#         prev = None 
#         while curr.next.next:
#             prev = curr 
#             curr = curr.next 
#         prev.next  = curr 
#         curr.next = None 

#     def insertAtFirst(self,data):
#         newData = Node(data)
#         if not self.head:
#             self.head = newData 
#             return 
#         curr = self.head 
#         self.head = newData 
#         self.head.next = curr 

#     def search(self,data):
#         if not self.head:
#             print("\nNo element to search")
#             return
        
#         if not self.head.next:
#             if self.head.data == data:
#                 print("\nFound at Index: 0")
#         index = 0
#         curr = self.head 
#         while curr:
#             if curr.data == data:
#                 print("\nFound at index: ", index)
#                 return 
#             index += 1
#             curr = curr.next 
#         else:
#             print(f"\n{data} Not found")
    
#     def hascycle(self,head):
#         slow = head 
#         fast = head 

#         while fast!=None and fast.next !=None:
#             slow = slow.next 
#             fast = fast.next.next 

#             if(slow == fast):
#                 return True 
#         else:
#             return False 
# a = Sll()
# a.search(2)
# a.appendData(1)
# a.appendData(2)
# a.appendData(3)
# a.appendData(4)
# a.printData()
# a.search(20)
# a.insertAtFirst(20)
# a.deleteAtLast()
# a.printData()
# a.deleteAtLast()
# a.printData().3

def bs(arr,val):
    left = 0
    right = len(arr)-1 

    while left<=right:
        mid = (left+right)//2 
        if arr[mid] == val:
            return mid 
        if arr[mid]<val:
            left = mid +1
        else:
            right = mid-1
    else:
        return -1 
def ls(arr,val):
    index = 0
    for i in arr:
        if i == val:
            return index 
        index += 1
# print(bs([1,2,3,4,5,6,7,8,9,10],5))
# print(ls([1,2,3,4,5,6,7,8,9,10],5))

def two_pointer(arr,target):
    left =0
    right = len(arr)-1
    while left<right:
        if arr[left]+arr[right] == target:
            return left, right 
        elif arr[left]+arr[right]<target:
            left += 1
        else:
            right -= 1 
    else:
        return -1 
print(two_pointer([1,2,3,4,5],9))

def three_sum(arr,tar):
    n = len(arr)
    arr.sort()
    for i in range(n-1):
        l = i + 1
        r = n - 1
        req = tar - arr[i]
        while l<r:
            if arr[l]+arr[r] == req:
                return True 
            elif arr[l]+arr[r]<req:
                l+=1
            else:
                r -=1
        else:
            return False 
print(three_sum([1,2,3,5,45,78,41,0,12],13))


















