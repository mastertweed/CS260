# Complete this class definition
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


def Inorder(node):
    if node:
        Inorder(node.left)
        print(node.val, end=" ")
        Inorder(node.right)
    else:
        print("N", end=" ")


def Preorder(node):
    if node:
        print(node.val, end=" ")
        Preorder(node.left)
        Preorder(node.right)
    else:
        print("N", end=" ")


def Postorder(node):
    if node:
        Postorder(node.left)
        Postorder(node.right)
        print(node.val, end=" ")
    else:
        print("N", end=" ")


def LorR(x, next):
    if next is None:
        return 0
    elif x == next.val:
        return 1
    elif x < next.val:
        return LorR(x, next.left)
    else:
        return LorR(x, next.right)


# It is recommended you create a node class and additional methods
class BST:
    def __init__(self):
        self.root = Node(None)

    def __str__(self):
        if self.root.val is None:
            return "Empty Tree"
        else:
            print("Preorder:", end=" ")
            Preorder(self.root)
            print('')
            print("Inorder:", end=" ")
            Inorder(self.root)
            print('')
            print("Postorder:", end=" ")
            Postorder(self.root)

            return ""


    def insert(self, x):
        if self.root.val is None:
            self.root = Node(x)

        else:
            pos = self.root
            flag = 0

            while flag == 0:
                if x == pos.val:
                    flag = 1
                elif x < pos.val:
                    if pos.left is None:
                        pos.left = Node(x)
                        flag = 1
                    else:
                        temp = pos.left
                        pos = temp

                elif x > pos.val:
                    if pos.right is None:
                        pos.right = Node(x)
                        flag = 1
                    else:
                        temp = pos.right
                        pos = temp

    def find(self, x):
        next = self.root

        if x == next.val:
            return True
        elif LorR(x, next) == 1:
            return True
        else:
            return False

