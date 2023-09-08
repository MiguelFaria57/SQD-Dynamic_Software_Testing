class Node:
    # constructor for Node class
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def newNode(key):
    # create a new node
    node = Node(key)
    return node


def rightRotate(x):
    # rotate the tree to the right
    y = x.left
    x.left = y.right
    y.right = x
    return y


def leftRotate(x):
    # rotate the tree to the left
    y = x.right
    x.right = y.left
    y.left = x
    return y


def splay(root, key, p=1):
    # perform the splay operation
    if p:
        print(1, end=",")
    if root is None or root.key == key:
        if p:
            print(2)
        return root
    if p:
        print(3, end=",")
    if root.key > key:
        if p:
            print(4, end=",")
        if root.left is None:
            if p:
                print(6)
            return root
        if p:
            print(7, end=",")
        if root.left.key > key:
            if p:
                print(10, end=",")
            root.left.left = splay(root.left.left, key, 0)
            root = rightRotate(root)
        elif root.left.key < key:
            if p:
                print(12, end=",")
                print(11, end=",")
            root.left.right = splay(root.left.right, key, 0)
            if p:
                print(14, end=",")
            if root.left.right:
                if p:
                    print(15, end=",")
                root.left = leftRotate(root.left)
        else:
            if p:
                print(12, end=",")
        if p:
            print(13)
        return (root.left is None) and root or rightRotate(root)
    else:
        if p:
            print(5, end=",")
        if root.right is None:
            if p:
                print(8)
            return root
        if p:
            print(9, end=",")
        if root.right.key > key:
            if p:
                print(17, end=",")
            root.right.left = splay(root.right.left, key, 0)
            if p:
                print(18, end=",")
            if root.right.left:
                if p:
                    print(19, end=",")
                root.right = rightRotate(root.right)
        elif root.right.key < key:
            if p:
                print(16, end=",")
                print(21, end=",")
            root.right.right = splay(root.right.right, key, 0)
            root = leftRotate(root)
        else:
            if p:
                print(16, end=",")
        if p:
            print(20)
        return (root.right is None) and root or leftRotate(root)


def execute_code_lines(selection):
    code_lines = {
        0: [
            "root = None",
            "splay(root, 0)"
        ],
        1: [
            "root = newNode(50)",
            "root = splay(root, 50)"
        ],
        2: [
            "root = newNode(50)",
            "root = splay(root, 30)"
        ],
        3: [
            "root = newNode(50)",
            "root = splay(root, 70)"
        ],
        4: [
            "root = newNode(50)",
            "root.left = newNode(30)",
            "root = splay(root, 20)"
        ],
        5: [
            "root = newNode(50)",
            "root.left = newNode(30)",
            "root = splay(root, 30)"
        ],
        6: [
            "root = newNode(50)",
            "root.left = newNode(30)",
            "root = splay(root, 35)"
        ],
        7: [
            "root = newNode(50)",
            "root.left = newNode(30)",
            "root.left.right = newNode(35)",
            "root = splay(root, 35)"
        ],
        8: [
            "root = newNode(50)",
            "root.right = newNode(70)",
            "root.right.left = newNode(65)",
            "root = splay(root, 65)"
        ],
        9: [
            "root = newNode(50)",
            "root.right = newNode(70)",
            "root = splay(root, 65)"
        ],
        10: [
            "root = newNode(50)",
            "root.right = newNode(70)",
            "root = splay(root, 70)"
        ],
        11: [
            "root = newNode(50)",
            "root.right = newNode(70)",
            "root = splay(root, 80)"
        ]
    }

    if selection in code_lines:
        return code_lines[selection]
    else:
        return []



if __name__ == '__main__':
    test = execute_code_lines(11)
    for line in test:
        exec(line)
