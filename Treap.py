import sys

class Node(object):
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.pai = None
        self.left = None
        self.right = None

class Treap(object):
    def __init__(self):
        self.root = None

    def __print_helper(self, currPtr, indent, last):
        # print the tree structure on the screen
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.data, currPtr.priority)

            self.__print_helper(currPtr.left, indent, False)
            self.__print_helper(currPtr.right, indent, True)

    def __search_tree_helper(self, node, key):
            if node == None or key == node.data:
                return node

            if key < node.data:
                return self.__search_tree_helper(node.left, key)
            return self.__search_tree_helper(node.right, key)

    # rotate left at node x
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.root = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y
        y.left = x
        x.pai = y

    # rotate right at node x
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.root = y
        elif x == x.pai.right:
            x.pai.right = y
        else:
            x.pai.left = y

        y.right = x
        x.pai = y

    # Splaying operation. It moves x to the root of the tree
    def moveUp(self, x):
        if x.pai == None:
            return
        elif x.priority <= x.pai.priority:
            return
        else:
            if x == x.pai.left:
                self.__right_rotate(x.pai)
            else:
                self.__left_rotate(x.pai)

        self.moveUp(x)


    # insert the key to the tree in its appropriate position
    def insert(self, key, priority):
        node = Node(key, priority)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.pai = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.moveUp(node)

    def pretty_print(self):
            self.__print_helper(self.root, "", True)

if __name__ == "__main__":


    bst = Treap()


    bst.insert(5, 0.30)
    bst.insert(7, 0.47)
    bst.insert(19, 0.54)
    bst.insert(23, 0.46)
    bst.insert(30, 0.73)
    bst.insert(31, 0.28)
    bst.insert(45, 0.99)
    bst.insert(48, 0.51)
    bst.insert(51, 0.98)
    bst.insert(25, 0.22)
    bst.pretty_print()