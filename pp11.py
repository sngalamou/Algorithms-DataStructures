def search(root,key): 
	if root is None or root.val == key: 
	    return root 

	if root.val < key: 
		return search(root.right,key) 
	return search(root.left,key)   
def insert(root, key): 
	if root is None: 
		return Node(key) 
	else: 
		if root.val == key: 
			return root 
		elif root.val < key: 
			root.right = insert(root.right, key) 
		else: 
			root.left = insert(root.left, key) 
def print_in_order(root): 
	if root: 
		print_in_order(root.left) 
		print(root.val) 
		print_in_order(root.right) 
