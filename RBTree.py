import sys

# Node creation
class Node:
    def __init__(self, item):
        self.item = item
        self.pai = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # faz a rotaçao para o lado esquerdo do node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.pai = x

        y.pai = x.pai
        if x.pai is None:
            self.root = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y
        y.left = x
        x.pai = y

    # faz a rotaçao para o lado direito do node x
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.pai = x

        y.pai = x.pai
        if x.pai is None:
            self.root = y
        elif x == x.pai.right:
            x.pai.right = y
        else:
            x.pai.left = y
        y.right = x
        x.pai = y

    # funçao para print em pre-ordem
    def _preorder(self, node):
        if node is not self.TNULL:
            sys.stdout.write(str(node.item) + " ")
            self._preorder(node.left)
            self._preorder(node.right)

    # funçao para print em ordem
    def _inorder(self, node):
        if node != self.TNULL:
            self._inorder(node.left)
            sys.stdout.write(str(node.item) + " ")
            self._inorder(node.right)

    # funçao para print em pos-ordem
    def _postorder(self, node):
        if node != self.TNULL:
            self._postorder(node.left)
            self._postorder(node.right)
            sys.stdout.write(str(node.item) + " ")

    # faz a procura recursiva na arvore
    def _procurar(self, node, key):
        if node == self.TNULL:
            print("O ELEMENTO "+str(key)+" NAO FOI ENCONTRADO")
            return
        elif key == node.item:
            print("O ELEMENTO "+str(key)+" FOI ENCONTRADO COM A COR ", "")
            if node.color == 1:
                print("VERMELHA")
            else:
                print("PRETA")
            return
        if key < node.item:
            return self._procurar(node.left, key)
        return self._procurar(node.right, key)

    # faz com que a arvore mantenha o equilibrio segundo as regras de construçao de uma arvore vermenlha e preta
    def _inserir(self, k):
        while k.pai.color == 1:
            if k.pai == k.pai.pai.right:
                u = k.pai.pai.left
                if u.color == 1:
                    u.color = 0
                    k.pai.color = 0
                    k.pai.pai.color = 1
                    k = k.pai.pai
                else:
                    if k == k.pai.left:
                        k = k.pai
                        self.rightRotate(k)
                    k.pai.color = 0
                    k.pai.pai.color = 1
                    self.leftRotate(k.pai.pai)
            else:
                u = k.pai.pai.right

                if u.color == 1:
                    u.color = 0
                    k.pai.color = 0
                    k.pai.pai.color = 1
                    k = k.pai.pai
                else:
                    if k == k.pai.right:
                        k = k.pai
                        self.leftRotate(k)
                    k.pai.color = 0
                    k.pai.pai.color = 1
                    self.rightRotate(k.pai.pai)
            if k == self.root:
                break
        self.root.color = 0

    def preorder(self):
        self._preorder(self.root)

    def inorder(self):
        self._inorder(self.root)

    def postorder(self):
        self._postorder(self.root)

    # inicia a procura pelo node K
    def procurar(self, k):
        return self._procurar(self.root, k)

    # inicia a inserçao da key na arvore
    def inserir(self, key):
        node = Node(key)
        node.pai = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.pai = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.pai is None:
            node.color = 0
            return

        if node.pai.pai is None:
            return

        self._inserir(node)







    # faz a construçao grafica da arvore
    def _printHelper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self._printHelper(node.left, indent, False)
            self._printHelper(node.right, indent, True)

    def printHelper(self):
        self._printHelper(self.root, "", True)










    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.pai.left:
                s = x.pai.right
                if s.color == 1:
                    s.color = 0
                    x.pai.color = 1
                    self.leftRotate(x.pai)
                    s = x.pai.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.pai
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.pai.right

                    s.color = x.pai.color
                    x.pai.color = 0
                    s.right.color = 0
                    self.leftRotate(x.pai)
                    x = self.root
            else:
                s = x.pai.left
                if s.color == 1:
                    s.color = 0
                    x.pai.color = 1
                    self.rightRotate(x.pai)
                    s = x.pai.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.pai
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.pai.left

                    s.color = x.pai.color
                    x.pai.color = 0
                    s.left.color = 0
                    self.rightRotate(x.pai)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.pai is None:
            self.root = v
        elif u == u.pai.left:
            u.pai.left = v
        else:
            u.pai.right = v
        v.pai = u.pai

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("O ELEMENTO "+str(key)+" NAO FOI ENCONTRADO")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.pai == z:
                x.pai = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.pai = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.pai = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.pai
        while y != self.TNULL and x == y.right:
            x = y
            y = y.pai
        return y

    def predecessor(self,  x):
        if x.left != self.TNULL:
            return self.maximum(x.left)

        y = x.pai
        while y != self.TNULL and x == y.left:
            x = y
            y = y.pai

        return y





    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)










if __name__ == "__main__":
    rb = RedBlackTree()

    info = ''

    while info != 'FIM':
        info = input()
        infoParsed = info.split(' ')
        if infoParsed[0] == 'A':
            rb.inserir(int(infoParsed[1]))
        if infoParsed[0] == 'C':
            rb.procurar(int(infoParsed[1]))
        if infoParsed[0] == 'L':
            rb.inorder()
            print("FIM")
        if infoParsed[0] == 'D':
            print("LISTAGEM DE NOMES APAGADA")
            root = None
