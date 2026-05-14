class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node == None:
        return []
    else:
        


if __name__ == '__main__':
    # tree = Node(4, 2, 9)
    print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3))))
