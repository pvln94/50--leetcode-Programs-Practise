# LCA of a BST

# Lowest Common Ancestor in a Binary Search Tree

# BST
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self._insert(self.root, x)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)  # Return the result of _search

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val, end=" ")
            self._inorder(root.right)

    def lca_bst(self,n1,n2):
        return self._lca_bst(self.root,n1,n2)
    
    def _lca_bst(self,root,n1,n2):
        if root is None:
            return None
        
        if root.val > n1 and root.val > n2:
            return self._lca_bst(root.left,n1,n2)
        
        if root.val < n1 and root.val < n2:
            return self._lca_bst(root.right,n1,n2)
        
        return root
        


# Example usage:
bst = BST()
bst.insert(5)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(1)

print("In-order traversal of the BST:")
bst.inorder()

found = bst.search(5)
if found:
    print(f"Found: {found.val}")
else:
    print("Not found")

# Find LCA
n1 = 5
n2 = 1
lca = bst.lca_bst(n1, n2)
if lca:
    print(f"LCA of {n1} and {n2} is {lca.val}")
else:
    print("LCA not found")
