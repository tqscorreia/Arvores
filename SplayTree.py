
class No:
    def __init__(self, nome, morada, valor):
        self.nome = nome
        self.morada = morada
        self.valor = valor
        self.pai = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, nome, morada, valor):
        no = No(nome, morada, valor)
        y = None
        x = self.root

        while x != None:
            y = x
            if no.nome < x.nome:
                x = x.left
            elif no.nome > x.nome:
                x = x.right
            elif nome == no.nome:
                print("CLIENTE JA EXISTENTE")
                return

        no.pai = y
        if y == None:
            self.root = no
        elif no.nome < y.nome:
            y.left = no
        else:
            y.right = no
        print("NOVO CLIENTE INSERIDO")
        self.splay(no)

    def ZAG(self, x):
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

    def ZIG(self, x):
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

    def splay(self, x):
        while x.pai != None:
            if x.pai.pai == None:
                if x == x.pai.left:
                    # zig rotation
                    self.ZIG(x.pai)
                else:
                    # zag rotation
                    self.ZAG(x.pai)
            elif x == x.pai.left and x.pai == x.pai.pai.left:
                # zig-zig rotation
                self.ZIG(x.pai.pai)
                self.ZIG(x.pai)
            elif x == x.pai.right and x.pai == x.pai.pai.right:
                # zag-zag rotation
                self.ZAG(x.pai.pai)
                self.ZAG(x.pai)
            elif x == x.pai.right and x.pai == x.pai.pai.left:
                # zig-zag rotation
                self.ZAG(x.pai)
                self.ZIG(x.pai)
            else:
                # zag-zig rotation
                self.ZIG(x.pai)
                self.ZAG(x.pai)

    def search(self, cliente):
        x = self.searchTree(self.root, cliente)
        if x != None:
            self.splay(x)

    def searchTree(self, no, cliente):
        if no == None:
            print("CLIENTE NAO REGISTADO")
            return
        elif no.nome == cliente:
            print(no.nome + " " + no.morada + " " + str(no.valor))
            print("FIM")
            return no

        elif cliente < no.nome:
            return self.searchTree(no.left, cliente)
        return self.searchTree(no.right, cliente)

    def atualiza(self, cliente, valor):
        x = self.atualizaTree(self.root, cliente, valor)
        if x != None:
            self.splay(x)

    def atualizaTree(self, no, cliente, valor):
        if no == None:
            print("CLIENTE NAO REGISTADO")
            return
        elif no.nome == cliente:
            no.valor += valor
            print("AQUISICAO INSERIDA")
            return no

        elif cliente < no.nome:
            return self.atualizaTree(no.left, cliente, valor)
        return self.atualizaTree(no.right, cliente, valor)

    def lista(self):
        self.listaTree(self.root)

    def listaTree(self, root):
        if not root:
            return
        self.listaTree(root.left)
        print(root.nome + " " + root.morada + " " + str(root.valor))
        self.listaTree(root.right)


if __name__ == "__main__":
    info = ''
    comandos = []
    while info != 'FIM':
        info = input()
        comandos.append(info)

    st = SplayTree()
    root = None

    i = 0
    while comandos[i] != 'FIM':

        infoParsed = comandos[i].split(' ')
        if infoParsed[0] == 'CLIENTE':
            m = infoParsed[2] + " " + infoParsed[3]
            st.insert(infoParsed[1], m, int(infoParsed[4]))
        if infoParsed[0] == 'AQUISICAO':
            st.atualiza(infoParsed[1], int(infoParsed[2]))
        if infoParsed[0] == 'CONSULTA':
            st.search(infoParsed[1])
        if infoParsed[0] == 'LISTAGEM':
            st.lista()
            print("FIM")
        if infoParsed[0] == 'APAGA':
            print("LISTAGEM DE CLIENTES APAGADA")
            root = None
        i += 1
