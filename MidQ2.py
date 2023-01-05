def checkforDuplicates(arr):
    arr.sort()
    for i in range (1, len(arr)):
        if arr[i] == arr[i-1]:
            return True;
    return False;


ourArray = [1,5]

print(checkforDuplicates(ourArray))
