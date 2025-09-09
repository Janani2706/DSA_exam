class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
print("Preorder Traversal (Recursive):")
preorder(root)