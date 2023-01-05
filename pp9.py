from datetime import datetime
from random import randint
def insertionSort(array):
    for i in array:
        a0 = array.index(i)
        while a0 > 0:
            if array[a0 - 1] > array[a0]:
                
                array[a0 - 1], array[a0] = array[a0], array[a0 - 1]
            else:
                break
            a0 -= 1
        
def __heapify(a, size, index):
   
    __max_data = index
    __left_data = 2 * index + 1
    __right_data = 2 * index + 2

    if __left_data < size and a[index] < a[__left_data]:
        __max_data = __left_data

    if __right_data < size and a[__max_data] < a[__right_data]:
        __max_data = __right_data

    if __max_data != index:
        a[index], a[__max_data] = a[__max_data], a[index]
        __heapify(a, size, __max_data)

def heapSort(a):
    size = len(a)

    for i in range(size, -1, -1):
        __heapify(a, size, i)

    for i in range(size - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        __heapify(a, i, 0) 
 
 
# Driver code to test above
number_of_items = 1000
array = [randint(10, 100) for _ in range(number_of_items)]
start = datetime.now()  
heapSort(array)  
end = datetime.now() 
elapsed = end-start  
print("Heap Sort time for {} items {}s {}ms".format(
    number_of_items, elapsed.seconds, elapsed.microseconds))
start = datetime.now()
insertionSort(array)
end = datetime.now()
elapsed = end - start
print("Insertion sort time for {} items {}s {}ms".format(
    number_of_items, elapsed.seconds, elapsed.microseconds))
