import sys

# Node creation
class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
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

    #faz a procura recursiva na arvore
    def _procura(self, node, key):
        if node == TNULL:
            print("ELEMENTO NAO ENCONTRADO")
        if key == node.item:
            return node

        if key < node.data:
            return self._procura(node.left, key)
        return self._procura(node.right, key)

    #reorganiza a arvore apos uma inserçao
    def _inserir(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # faz a listagem recursiva na arvore
    def _lista(self, node):
        if node != TNULL:
            self._lista(node.left)
            sys.stdout.write(node.data + " ")
            self._lista(node.right)

    #faz a rotaçao para o lado esquerdo do node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    #faz a rotaçao para o lado direito do node x
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    #inicia a procura pelo node K
    def procura(self, k):
        return self._procura(self.root, k)

    #inicia a inserçao da key na arvore
    def inserir(self, key):
        node = Node(key)
        node.parent = None
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

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self._inserir(node)

    def lista(self):
        self._lista(self.root)



if __name__ == "__main__":
    rb = RedBlackTree()
    info = ''

    while info != 'FIM':
        info = input()
        infoParsed = info.split(' ')
        if infoParsed[0] == 'ACRESCENTA':
            rb.inserir(int(infoParsed[1]))
        if infoParsed[0] == 'CONSULTA':
            rb.procura(int(infoParsed[1]))
        if infoParsed[0] == 'LISTAGEM':
            rb.lista()
            print("FIM")
        """if infoParsed[0] == 'APAGA':
            print("ARVORE APAGADA")
            root = None

    rb.insert(8)
    rb.insert(18)


    rb.print_tree()"""
