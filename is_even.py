def is_even(x:int):
    assert type(x) == int
    return (x&1 == 0)

print (is_even(2))


def sumsquares(k):
    return (sum(x*x for x in range(1, k)))

print (sumsquares(2))  #want to add up 1*1
print (sumsquares(10)) # want to add up 1*1, 2*2, etc.
