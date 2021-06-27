
class No(object):

    def __init__(self, num, vacina, data):
        self.num = num
        self.vacina = [[vacina, data]]
        self.dir = None
        self.esq = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None

    def inserir(self, root, num, vacina, data):
        if root is None:
            print("NOVO UTENTE CRIADO")
            return No(num, vacina, data)
        elif num < root.num:
            root.esq = self.inserir(root.esq, num, vacina, data)

        elif num > root.num:
            root.dir = self.inserir(root.dir, num, vacina, data)

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

        root.height = 1 + max(self.altura(root.esq),
                              self.altura(root.dir))

        fator = self.equilibrio(root)
        if fator > 1:
            if self.equilibrio(root.esq) >= 0:
                return self.rightRotate(root)
            else:
                root.esq = self.leftRotate(root.esq)
                return self.rightRotate(root)

        if fator < -1:
            if self.equilibrio(root.dir) <= 0:
                return self.leftRotate(root)
            else:
                root.dir = self.rightRotate(root.dir)
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
            return self.procura(root.dir, key)
        elif root.num > key:
            return self.procura(root.esq, key)

    def equilibrio(self, root):
        if not root:
            return 0
        return self.altura(root.esq) - self.altura(root.dir)

    def leftRotate(self, z):
        y = z.dir
        T2 = y.esq
        y.esq = z
        z.dir = T2
        z.height = 1 + max(self.altura(z.esq),
                           self.altura(z.dir))
        y.height = 1 + max(self.altura(y.esq),
                           self.altura(y.dir))
        return y

    def rightRotate(self, z):
        y = z.esq
        T3 = y.dir
        y.dir = z
        z.esq = T3
        z.height = 1 + max(self.altura(z.esq),
                           self.altura(z.dir))
        y.height = 1 + max(self.altura(y.esq),
                           self.altura(y.dir))
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
