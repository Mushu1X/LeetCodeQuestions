class Node:
    def __init__ (self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(tree1, tree2):

    if tree1 is None and tree2 is None:
        return True
    
    if tree1 is None or tree2 is None:
        return False

    return is_same_tree(tree1.val, tree2.val) or is_same_tree(tree1.left, tree2.left) or is_same_tree(tree1.right, tree2.right)

def subtree(root: Node, sub_root: Node):

    if not root:
        return False
    
    return subtree(root.left, sub_root) or subtree(root.right, sub_root) or is_same_tree(root, sub_root)



def build_tree(nodes, f):
    val = next(nodes)

    if val == "x":
        return None
    
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)

    return Node(f(val), left, right)
