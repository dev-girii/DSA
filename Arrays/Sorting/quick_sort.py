def quick_sort(arr):
    if len(arr)<=1:
        return arr 
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]

    return quick_sort(left) + middle + quick_sort(right)
arr = [2,41,4,4,11,24,5,86,35,15,32,184,264,4547]
print(quick_sort(arr))
# print(sorted(arr))