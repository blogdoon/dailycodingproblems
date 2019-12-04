class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


def count_unival_tree(node, count):

    if node == None:
         return True

    left = count_unival_tree(node.left, count)
    right = count_unival_tree(node.right, count)

    if left ==False or right == False:
        return True
    
    if node.left and node.data != node.left.data:
        return False

    if node.right and node.data != node.right.data:
        return False

    

    count[0] += 1
    return True

def count_single_unival():
    count = [0]

    root = Node(5) 
    root.left = Node(4) 
    root.right = Node(5) 
    root.left.left = Node(4) 
    root.left.right = Node(4) 
    root.right.right = Node(5) 


    count_unival_tree(root, count)

    print(count[0])


count_single_unival()

