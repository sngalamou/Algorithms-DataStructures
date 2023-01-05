class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next
        def __init__(self):
            self._head = self._tail = None
        def is_palindrome(self)->bool:
            if self._head != self._tail:
                return false
            if self == self[::-1]:
                return true

        


