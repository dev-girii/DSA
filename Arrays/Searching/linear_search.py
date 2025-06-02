def ls(arr,val):
    index = 0
    for i in arr:
        if i == val:
            return index
        index += 1
    else:
        return -1
print(ls([1,2,3,4],10))