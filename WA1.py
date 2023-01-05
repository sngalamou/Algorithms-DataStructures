def is_even(x:int):
    assert type(x) == int
    return (x&1 == 0)

print (is_even(2))


def sumsquares(k):
    return (sum(x*x for x in range(1, k)))

print (sumsquares(10)) # want to add up 1*1, 2*2, etc.

def all_unique(array):
    num_set = set()
    for number in array:
        if number in num_set:
            return False
        else:
            num_set.add(number)
    return True

data = [1,2,3,4,5,6]; print (all_unique(data))

def scale(data, factor):
    for val in data:
        val *= factor
print('Bad scaling')        
data = [1,2,3,4,5]; print (data)
scale(data, 5); print (data)

def realscale(data, factor):
    #data*=factor #This will concatenate the array with itself multiple times!  
    for i in range (len(data)):
        data[i]*=factor

print ('\nGood scaling')
data = [1,2,3,4,5]; print (data)
realscale(data, 5); print (data)


