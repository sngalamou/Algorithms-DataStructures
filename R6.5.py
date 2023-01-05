class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = self._tail = None


    def find_median(self):
        x = self._head
        y = self._head
        while(y is not None and y._next is not None):
            x = x._next
            y = y._next._next
        return x._element


