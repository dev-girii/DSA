def three_sum(arr,tar):
    n = len(arr)
    for i in range(n-1):
        left = i + 1
        right = n -1 

        req_sum = tar - arr[i]
        while left<right:
            if arr[left]+ arr[right] == req_sum:
                return True 
            elif arr[left] + arr[right] < req_sum:
                left+= 1
            else:
                right -= 1
        else:
            return False 
print(three_sum([1,2,3,4,5,6,7],6))