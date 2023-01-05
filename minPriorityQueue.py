class P:
#Abstract base class for a priority queue.
    class Item:
        __slots__ = '_key' , '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self. key < other. key # compare items based on their keys

    def is_empty(self): # concrete method assuming abstract len
        return len(self) == 0
P.add(5,A)
