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


# function tree_to_tuple that converts a binary tree into a tuple representing the same tree.
def tree_to_tuple(node):
  if isinstance(node, TreeNode):  
    if node.left is None and node.right is None:
      return node.key

    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right) )


#helper function to display all the keys in a tree-like structure for easier visualization.
def display_keys(node, space='\t', level=0):
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1) 
