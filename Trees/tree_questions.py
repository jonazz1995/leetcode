
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def isbalanced(root):

    if not root:
        return True
    
    left_h = height(root.left)
    right_h = height(root.right)

    if abs(left_h - right_h) <= 1 and isbalanced(root.left) and isbalanced(root.right):
        return True

    return False
