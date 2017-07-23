class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    return miniCheck(root, -1, 11000)


def miniCheck(root, min, max):
    if root == None:
        return True
    d = root.data
    if d <= min or d >= max:
        return False
    else:
        return miniCheck(root.left, min, d) and miniCheck(root.right, d, max)
