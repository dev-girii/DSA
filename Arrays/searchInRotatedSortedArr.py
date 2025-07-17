def searchInRotArr(arr, tar):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[r]:
            r = m
        else:
            l = m + 1
    pivot = l

    def bs(l, r):
        while l <= r:
            m = (l+ r)// 2
            if arr[m] == tar:
                return m 
            if arr[m] > tar:
                r = m - 1 
            else:
                l = m + 1 
        else:
            return -1 
    result = bs(0, pivot)
    if result != -1:
        return result
    return bs(pivot, len(arr)-1)

print(searchInRotArr([6,7,8,9,1,2,3,4,5],5))