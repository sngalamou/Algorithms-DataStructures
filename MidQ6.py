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

if __name__== '__main__':
    llist = SinglyList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth=Node(4);
    fifth=Node(5);
    sixth=Node(7)
    llist.head.next = second;
    second.next = third;
    third.next=fourth;
    fourth.next=fifth;
    fifth.next=sixth
    llist.listprint()
