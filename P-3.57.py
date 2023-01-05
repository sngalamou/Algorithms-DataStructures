# TimSort
RUN = 32 #run is initialised to 32.
  
# sorting function
def insertionSort(arr, left, right):

   for i in range(left + 1, right+1):
  
       temp = arr[i] #storing in temp
       j = i - 1
       while arr[j] > temp and j >= left: #condition check
      
           arr[j+1] = arr[j]
           j -= 1
      
       arr[j+1] = temp
  
# merge function to merge
def merge(arr, l, m, r): #function

   # there is two parts of orginal array ,left and rigth
   #they are joined here
   len1, len2 = m - l + 1, r - m #lengths
   left, right = [], [] #sub arrays
   for i in range(0, len1): #appendindg to left sub array
       left.append(arr[l + i])
   for i in range(0, len2): #appendindg to right sub array
       right.append(arr[m + 1 + i])
  
   i, j, k = 0, 0, l
   # comparison for merging
   while i < len1 and j < len2:
  
       if left[i] <= right[j]: #checking condition 1
           arr[k] = left[i]
           i += 1
      
       else: #checking condition 1
           arr[k] = right[j]
           j += 1
      
       k += 1 #increment k
  
   # cpoying the other elements remaining of left
   while i < len1:
  
       arr[k] = left[i] #assigning
       k += 1 #increment
       i += 1
  
   # cpoying the other elements remaining of left
   while j < len2:
       arr[k] = right[j] #assigning
       k += 1 #increment
       j += 1
  
# Tims sort
def timSort(arr, n):

   # sort each sub array
   for i in range(0, n, RUN):
       insertionSort(arr, i, min((i+31), (n-1))) #insertion sort call
  
   # merging
   size = RUN
   while size < n:
  
       # do while size<n
       for left in range(0, n, 2*size):
      
           # midpoint found
           mid = left + size - 1
           right = min((left + 2*size - 1), (n-1))
  
           # merging
           merge(arr, left, mid, right)
      
       size = 2*size
      
# printing array
def printArray(arr, n):

   for i in range(0, n):
       print(arr[i], end = " ")
   print()

  
arr = [10,20,15,14,13] #array
n = len(arr)#length
print("Given Array is")
printArray(arr, n) #function call

timSort(arr, n) #sorting

print("After Sorting Array is") #print
printArray(arr, n) #call
