
class No(object):

    def __init__(self, num, vacina, data):
        self.num = num
        self.vacina = [[vacina, data]]
        self.right = None
        self.left = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None

    def inserir(self, root, num, vacina, data):
        if root is None:
            print("NOVO UTENTE CRIADO")
            return No(num, vacina, data)
        elif num < root.num:
            root.left = self.inserir(root.left, num, vacina, data)

        elif num > root.num:
            root.right = self.inserir(root.right, num, vacina, data)

        elif num == root.num:
            cond = True
            for i in range(len(root.vacina)):
                if vacina == root.vacina[i][0]:
                    print("VACINA ATUALIZADA")
                    root.vacina = [[vacina, data]]
                    cond = False
                    break
            if cond is True:
                print("NOVA VACINA INSERIDA")
                root.vacina.append([vacina, data])

        root.height = 1 + max(self.altura(root.left),
                              self.altura(root.right))

        fator = self.equilibrio(root)
        if fator > 1:
            if self.equilibrio(root.esq) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if fator < -1:
            if self.equilibrio(root.dir) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def procura(self, root, key):
        if root is None:
            print("NAO ENCONTRADO")
            return
        elif root.num == key:
            if len(root.vacina) >= 1:
                v = sorted(root.vacina)
                print(str(root.num), end=' ')
                for i in range(len(v)):
                    out = v[i][0] + " " + str(v[i][1])
                    print(out, end=' ')
                print()
                print("FIM")

            return

        elif root.num < key:
            return self.procura(root.right, key)
        elif root.num > key:
            return self.procura(root.left, key)

    def equilibrio(self, root):
        if not root:
            return 0
        return self.altura(root.left) - self.altura(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.altura(z.left),
                           self.altura(z.right))
        y.height = 1 + max(self.altura(y.left),
                           self.altura(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.altura(z.left),
                           self.altura(z.right))
        y.height = 1 + max(self.altura(y.left),
                           self.altura(y.right))
        return y

    def altura(self, root):
        if not root:
            return 0
        return root.height

    def lista(self, root):
        if not root:
            return
        self.lista(root.esq)
        if len(root.vacina) >= 1:
            v = sorted(root.vacina)
            print(str(root.num), end=' ')
            for i in range(len(v)):
                out = v[i][0] + " " + str(v[i][1])
                print(out, end=' ')
            print()
        else:
            out = str(root.num) + " " + root.vacina[0][0] + " " + str(root.vacina[0][1])
            print(out)
        self.lista(root.dir)


if __name__ == "__main__":
    avl = AVLTree()
    root = None
    info = ''

    while info != 'FIM':
        info = input()
        infoParsed = info.split(' ')
        if infoParsed[0] == 'ACRESCENTA':
            root = avl.inserir(root, int(infoParsed[1]), infoParsed[2], int(infoParsed[3]))
        if infoParsed[0] == 'CONSULTA':
            avl.procura(root, int(infoParsed[1]))
        if infoParsed[0] == 'LISTAGEM':
            avl.lista(root)
            print("FIM")
        if infoParsed[0] == 'APAGA':
            print("LISTAGEM DE NOMES APAGADA")
            root = None
