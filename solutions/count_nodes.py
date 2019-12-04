class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")

d = Node("d")
e = Node("e")

a.left = b
a.right = c

b.left = d
b.right = e

def count_nodes(root):
    return count_nodes(root.left) + count_nodes(root.right) + 1 if root else 0

print(count_nodes(a))


def deepest_node(node, depth):
    if node.left == None and node.right:


    elif node.right == None and node.left:
        deepest_node((node.right,))

    return max(deepest_node(node.left), deepest_node(node.right), key = lambda x: x[1])




def increament_depth(node_tuple):
    return (node_tuple[0], node_tuple[1] + 1)

