class Node:
    # The class represents a single node in a binary tree 
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

# modelling the above binary tree 
tree = Node(7)

tree.left_child = Node(3)

tree.left_child.left_child = Node(2)
tree.left_child.right_child = Node(5)

tree.left_child.left_child.left_child = Node(4)
tree.left_child.left_child.left_child.left_child = Node(19)

tree.left_child.right_child.right_child = Node(7)
tree.left_child.right_child.right_child.right_child = Node(10)
tree.left_child.right_child.right_child.right_child.right_child = Node(20)


tree.right_child = Node(11)
tree.right_child.left_child = Node(6)
tree.right_child.right_child = Node(14)

tree.right_child.left_child.left_child = Node(9)
tree.right_child.left_child.right_child = Node(1)

tree.right_child.left_child.left_child.left_child = Node(11) 
tree.right_child.left_child.left_child.left_child.left_child = Node(21)
tree.right_child.left_child.left_child.left_child.right_child = Node(24)


tree.right_child.right_child.left_child = Node(12)
tree.right_child.right_child.right_child = Node(16)

# traverses tree and prints value of each node
def print_nodes(root: Node):
	print(root.value)
	
	if root.left_child is not None:
		print_nodes(root.left_child)
	if root.right_child is not None:
		print_nodes(root.right_child)

def greatest_node(root: Node):
    value = root.value

    if root.left_child is not None:
        l_greatest = greatest_node(root.left_child)
        if value < l_greatest:
            value = l_greatest
    if root.right_child is not None:
        r_greatest = greatest_node(root.right_child)
        if value < r_greatest:
            value = r_greatest
    print(value)
    return value

#print_nodes(tree)
#print(greatest_node(tree))

def tree_depth(root: Node):
    if root is None:
        return 0
    
    l_depth = tree_depth(root.left_child)
    r_depth = tree_depth(root.right_child)
    
    return max(l_depth, r_depth) + 1

node_location = {}
# Populates dictionary node_location:
# Key = root depth (d); 
# Value = dictionary of indices:
    # Key = index (0 –> d^2 - 1)
    # Value = node value
# Tree structure:
# d: i: 
# 0  0
#    |___
#    |   |  
# 1  0   1
#    |_  |_ 
#    | | | |
# 2  0 1 2 3
# NB: for node at index i, it's children have indices 2i and 2i + 1
def index_nodes(root: Node, depth: int, index: int):
    try:
        node_location[depth]
    except KeyError:
        node_location[depth] = {i: -1 for i in range(0, 2**depth)}
    
    node_location[depth][index] = root.value

    if root.left_child is not None:
        l_loc = 2*index
        index_nodes(root.left_child, depth+1, l_loc)
    if root.right_child is not None:
        r_loc = 2*index + 1
        index_nodes(root.right_child, depth+1, r_loc)

def print_tree(root):
    d_max = tree_depth(tree)

    for d in node_location:
        for i in node_location[d]:
            # only print occupied nodes (ie not -1)
            if node_location[d][i] != -1:
                print(f"{' '*(2**(d_max - d) -1)}{node_location[d][i]:2d}{' '*(2**(d_max - d) -1)}", end="")
            else:
                print(f"{' '*(2**(d_max - d) -1)}  {' '*(2**(d_max - d) -1)}", end="")
        print()
        if d+1 != d_max:
            for i in node_location[d]:
                # node has two children
                if node_location[d+1][2*i] != -1 and node_location[d+1][2*i+1] != -1:
                    print(f"{' '*(2**((d_max-d)-1))}{'_'*(2**((d_max-d)-1)-1)}{' |'}{'_'*2**((d_max-d)-1)}{' '*(2**((d_max-d)-1)-1)}", end="")
                # node has only left child
                elif node_location[d+1][2*i] != -1:
                    print(f"{' '*(2**((d_max-d)-1))}{'_'*(2**((d_max-d)-1)-1)}{' |'}{' '*2**((d_max-d)-1)}{' '*(2**((d_max-d)-1)-1)}", end="")
                # node has only right child
                elif node_location[d+1][2*i+1] != -1:
                    print(f"{' '*(2**((d_max-d)-1))}{' '*(2**((d_max-d)-1)-1)}{' |'}{'_'*2**((d_max-d)-1)}{' '*(2**((d_max-d)-1)-1)}", end="")
                else:
                    print(f"{' '*(2**((d_max-d)-1)-1)}{' '*2**((d_max-d)-1)}{'  '}{' '*2**((d_max-d)-1)}{' '*(2**((d_max-d)-1)-1)}", end="")
        print()


index_nodes(tree, 0, 0)
for node in node_location:
    print(node, node_location[node])
print_tree(tree)




