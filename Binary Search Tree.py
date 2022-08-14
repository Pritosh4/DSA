class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        
# helper function which can convert a tuple with the structure ( left_subtree, key, right_subtree) to binary tree

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
