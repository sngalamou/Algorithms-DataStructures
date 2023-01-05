class BinaryTree:
    class _Node:
        def __init__(self, e, left = None, right = None, data = None):
            self._left = left
            self._right = right
            self._element = e
            self.data=data


    def __init__(self):
        self._root = None
        self._size = 0

    def is_empty(self):
        return self._root == None

    def add_root(self, e):
        if self._root:
            return None

        self._root = self._Node(e)
        return self._root

    def add_left(self, e, p):
        p._left = self._Node(e)
        return p._left

    def add_right(self, e, p):
        p._right = self._Node(e)

        return p._right

    def _height(self, v):
        if not v:
            return -1

        x = self._height(v._left)
        y = self._height(v._right)
        return 1 + max(x, y)


    def height(self):
        return self._height(self._root)

    def _inOrder(self, p):
        if p:
            self._inOrder(p._left)
            print(p._element)
            self._inOrder(p._right)

    def inOrder(self):
        self._inOrder(self._root)

    def _preOrder(self, p):
        if p:
            print(p._element)
            self._preOrder(p._left)
            self._preOrder(p._right)

    def preOrder(self):
        self._preOrder(self._root)


    def _postOrder(self, p):
        if p:
            self._postOrder(p._left)
            self._postOrder(p._right)
            print(p._element)

    def postOrder(self):
        self._postOrder(self._root)


    def equal(self, other):
        return self._equal(self._root, other._root)

    def _equal(self, root1, root2):
        if root1 is None and root2 is None: 
            return True 
        if root1 is not None and root2 is not None: 
            return ((root1._element == root2._element) and 
                    self._equal(root1._left, root2._left) and
                    self._equal(root1._right, root2._right)) 
        return False

    def count(self, num):
        current = self._root  
        stack = [] 
        count = 0 
        while True:  
            if current is not None: 
                stack.append(current) 
                current = current._left  
            elif(stack): 
                current = stack.pop() 
                if current._element == num:
                    count = count + 1
                current = current._right  
            else: 
                break
        return count




x = BinaryTree()
root = x.add_root(10)
left_child = x.add_left(5, root)
x.add_right(7, root)
x.add_left(8, left_child)
x.add_right(2, left_child)


y = BinaryTree()
root = y.add_root(10)
left_child = y.add_left(5, root)
y.add_right(7, root)
y.add_left(8, left_child)
y.add_right(2, left_child)


z = BinaryTree()
root = z.add_root(10)
left_child = z.add_left(5, root)
z.add_right(7, root)
z.add_left(10, left_child)
z.add_right(5, left_child)


print(z.height())
print(z.count(10))



if(x.equal(y)):
    print("x and y are equal")
else:
    print("x and y are not equal")

if(y.equal(z)):
    print("y and z are equal")
else:
    print("y and z are not equal")
