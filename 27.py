# LCA of a Binary Tree

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = Node(data)
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = Node(data)
                break
            else:
                queue.append(node.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return root

        left_search = self._search(root.left, key)
        if left_search is not None:
            return left_search

        return self._search(root.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val, end=" ")
            self._inorder(root.right)

    def find_lca(self, n1, n2):
        return self._find_lca(self.root, n1, n2)

    def _find_lca(self, root, n1, n2):
        if root is None:
            return None

        if root.val == n1 or root.val == n2:
            return root

        left_lca = self._find_lca(root.left, n1, n2)
        right_lca = self._find_lca(root.right, n1, n2)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

# Example usage:
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("In-order traversal of the Binary Tree:")
bt.inorder()

found = bt.search(5)
if found:
    print(f"Found: {found.val}")
else:
    print("Not found")

# Find LCA
n1 = 4
n2 = 5
lca = bt.find_lca(n1, n2)
if lca:
    print(f"LCA of {n1} and {n2} is {lca.val}")
else:
    print("LCA not found")
