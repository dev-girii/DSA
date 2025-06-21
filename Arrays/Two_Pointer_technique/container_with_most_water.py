def containerWithMostWater(arr):
    n = len(arr)
    l = 0
    r = n - 1
    max_area = 0
    while l<r:
        w = (r-l) * min(arr[l], arr[r])
        max_area = max(max_area, w)

        if arr[l]< arr[r]:
            l += 1
        else:
            r-= 1
    return max_area

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))