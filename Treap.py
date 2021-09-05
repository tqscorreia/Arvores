import sys


class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.pai = None
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    # faz a rotaçao para o lado esquerdo do node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
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
        if y.right is not None:
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
        if node is not None:
            sys.stdout.write(str(node.item) + " ("+str(node.priority)+")  ")
            self._preorder(node.left)
            self._preorder(node.right)

    # funçao para print em ordem
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            sys.stdout.write(str(node.item) + " ("+str(node.priority)+")  ")
            self._inorder(node.right)

    # funçao para print em pos-ordem
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            sys.stdout.write(str(node.item) + " (" + str(node.priority) + ")  ")

    # faz a procura recursiva na arvore
    def _procurar(self, node, key):
        if node is None:
            print("ELEMENTO "+str(key)+" NAO ENCONTRADO")
            return
        elif key == node.item:
            print("ELEMENTO "+str(key)+" ENCONTRADO")
            return node
        if key < node.data:
            return self._procurar(node.left, key)
        return self._procurar(node.right, key)

    # faz com que a arvore mantenha o equilibrio segundo as regras de construçao de uma treap
    def moveUp(self, x):
        if x.pai is None:
            return
        elif x.priority <= x.pai.priority:
            return
        else:
            if x == x.pai.left:
                self.rightRotate(x.pai)
            else:
                self.leftRotate(x.pai)

        self.moveUp(x)

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
    def inserir(self, key, priority):
        node = Node(key, priority)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.pai = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.moveUp(node)







    # faz a construçao grafica da arvore
    def _printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.item, currPtr.priority)

            self._printHelper(currPtr.left, indent, False)
            self._printHelper(currPtr.right, indent, True)

    def printHelper(self):
        self._printHelper(self.root, "", True)



if __name__ == "__main__":
    t = Treap()

    t.inserir(5, 0.30)
    t.inserir(7, 0.47)
    t.inserir(19, 0.54)
    t.inserir(23, 0.46)
    t.inserir(30, 0.73)
    t.inserir(31, 0.28)
    t.inserir(45, 0.99)
    t.inserir(48, 0.51)
    t.inserir(51, 0.98)
    t.inserir(25, 0.22)
    t.printHelper()

"""
    info = ''

    while info != 'FIM':
        info = input()
        infoParsed = info.split(' ')
        if infoParsed[0] == 'ACRESCENTA':
            t.inserir(int(infoParsed[1]), int(infoParsed[2]))
        if infoParsed[0] == 'CONSULTA':
            t.procurar(int(infoParsed[1]))
        if infoParsed[0] == 'LISTAGEM':
            t.inorder()
            print("FIM")
        if infoParsed[0] == 'APAGA':
            print("LISTAGEM DE NOMES APAGADA")
            root = None
            """