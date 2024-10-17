class Node:

    def __init__(self, val, left = None, right= None):

        self.val = val 
        self.left = left
        self.right = right


def in_order_trav(root: None):

    if root is not None:
        in_order_trav(root.left)
        print(root.val)
        in_order_trav(root.right)

def pre_order(root: None):

    if root is not None:

        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


def post_order(root: None):
    if root is not None:
            
        post_order(root.left)
        post_order(root.right)
        print(root.val)


def dfs(root, target):
    
    if root is None:
        return None
    
    if root.val == target:
        return root
    
    left = dfs(root.left, target)
    if left is not None:
        return left
    
    return dfs(root.right, target):

def build_tree(nodes, f):

    val = next(nodes)
    if val == "x":
        return None
    
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)

    return Node(f(val), left, right)


if __name__ == "__main__":

    root = build_tree(iter(input().split()), int)

    in_order_trav(root)
