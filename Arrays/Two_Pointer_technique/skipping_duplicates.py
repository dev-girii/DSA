def skip_duplicates(arr):
    wi = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[wi] = arr[i]
            wi += 1
    return wi 
arr = [1,1,2,2,3,3,4,4]
print(arr[:skip_duplicates(arr)])