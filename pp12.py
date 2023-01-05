def inversions(L: list) -> int:
    count = 0 
    for i in range(len(L)-1):
        if(L[i]>L[i+1]):
            count=count+1 
    return count 

list = [4,3,4,6,5,6,7,8,7]
print(inversions(list))
