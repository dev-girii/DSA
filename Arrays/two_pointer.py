def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


def two_sum_unsorted(arr,target):
    ind_map = {}
    for i, num in enumerate(arr):
        diff = target - num 
        if diff in ind_map:
            return (ind_map[diff], i)
        ind_map[num] = i 
        print(ind_map)
    return None
print(two_sum_unsorted([1,21,4,14,5],19))