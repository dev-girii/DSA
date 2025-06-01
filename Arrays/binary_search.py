def bs(arr,val):
    left = 0
    right = len(arr) -1

    while left<=right:
        mid = (left+right)//2 

        if arr[mid] == val:
            return mid 
        if arr[mid]<val:
            left = mid+1
        else:
            right = mid-1
    return -1 
a = [1,2,3,4,5,6,7]
print(bs(a,15)) 
        