def stocks(arr):
    l = 0
    r = 1
    maxP = 0
    while r < len(arr):
        if arr[l]<arr[r]:
            profit = arr[r] - arr[l]
            print(arr[r], arr[l])
            maxP = max(profit, maxP)
        else:
            l = r 
        r += 1 
    return maxP, l, r

print(stocks([7,6,4,3,1]))