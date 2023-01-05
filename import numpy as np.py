#R6.5
class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return str(self._data)
    def is_empty(self):
        return len(self._data)
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def reverse_stack(list,stack):
    for line in list:
        stack.push(line)
        print(stack)

l = [1,2,3,4,5]
S= ArrayStack()