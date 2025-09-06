class Node:
    # The class represents a single node in a binary tree 
    def __init__(self, value, parent:'Node' = None, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

def tree_crawler(root):
    global tree
    print(root.value)
    print_tree(tree, root.value)
    print("Current node: ", root.value)

    print("Enter command: ")
    print("0 to exit")
    print("1 to go left")
    print("2 to go right")
    print("3 to go up")

    cmd = input()

    if cmd not in ["0", "1", "2", "3"]:
        print("Invalid input")
        # reload current node
        return tree_crawler(root)
    
    if cmd == "1":
        if root.left_child is not None:
            # left child becomes selected node, current node becomes parent
            return tree_crawler(root.left_child)
        print("No left child")
        # reload current node
        return tree_crawler(root)
    
    if cmd == "2":
        if root.right_child is not None:
            # right child becomes selected node, current node becomes parent
            return tree_crawler(root.right_child)
        print("No right child")
        # reload current node
        return tree_crawler(root)
    
    if cmd == "3":
        # load parent node, if there is one
        if root.parent != None:
            return tree_crawler(root.parent)
        print("This is the seed")
        return tree_crawler(root)
    
    return root.value

def tree_depth(root: Node):
    if root is None:
        return 0
    
    l_depth = tree_depth(root.left_child)
    r_depth = tree_depth(root.right_child)
    
    return max(l_depth, r_depth) + 1

node_location = {}

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

def print_tree(root, selected: int = None):
    d_max = tree_depth(tree)

    for d in node_location:
        for i in node_location[d]:
            # only print occupied nodes (ie not -1)
            if node_location[d][i] != -1:
                if node_location[d][i] == selected:
                    print(f"{' '*(2**(d_max - d) -2)}>{node_location[d][i]:2d}<{' '*(2**(d_max - d) -2)}", end="")
                else:
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

tree = Node(7)

tree.left_child = Node(3, tree)

tree.left_child.left_child = Node(2, tree.left_child)
tree.left_child.right_child = Node(5, tree.left_child)

tree.left_child.left_child.left_child = Node(4, tree.left_child.left_child)
tree.left_child.left_child.left_child.left_child = Node(19, tree.left_child.left_child.left_child)

tree.left_child.right_child.right_child = Node(17, tree.left_child.right_child)

tree.left_child.right_child.right_child.right_child = Node(10, tree.left_child.right_child.right_child)
tree.left_child.right_child.right_child.right_child.right_child = Node(20, tree.left_child.right_child.right_child.right_child)


tree.right_child = Node(11, tree)
tree.right_child.left_child = Node(6, tree.right_child)
tree.right_child.right_child = Node(14, tree.right_child)

tree.right_child.left_child.left_child = Node(9, tree.right_child.left_child)
tree.right_child.left_child.right_child = Node(1, tree.right_child.left_child)

tree.right_child.left_child.left_child.left_child = Node(1, tree.right_child.left_child.left_child) 
tree.right_child.left_child.left_child.left_child.left_child = Node(21, tree.right_child.left_child.left_child.left_child)
tree.right_child.left_child.left_child.left_child.right_child = Node(24, tree.right_child.left_child.left_child.left_child)


tree.right_child.right_child.left_child = Node(12, tree.right_child.right_child)
tree.right_child.right_child.right_child = Node(16, tree.right_child.right_child)

index_nodes(tree, 0, 0)
tree_crawler(tree)