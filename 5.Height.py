class Tree:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
def getHeight(root):
    if root is None:
        return -1  
 
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
 
    return max(left_height, right_height) + 1
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.left.left.left = Tree(7)
root.right.left.left = Tree(8)
 
print("Height of tree is:", getHeight(root))