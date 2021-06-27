import random
from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

def geraTransacao(n):
    transactions = []

    for i in range(n):
        num = random.randint(101012007, 999931122100)
        transactions.append(num)
    return transactions

def one_hash(hash1):
    h = hash1 % 1000000007
    return h

def sum_hash(hash1, hash2):
    h1 = hash1 % 1000000007
    h2 = hash2 % 1000000007
    h = (h1 + h2) % 1000000007
    return h

def MerkleTree(transacoes):
    global nivel
    transacoesCode = []
    if len(transacoes) == 1:
        if nivel == 0:
            for i in range(len(transacoes)):
                transacoesCode.append(one_hash(transacoes[i]))
            mTree.append(transacoesCode)
            nivel = +1

        comp = len(mTree)
        for c in range(comp):
            for q in range(len(mTree[comp - c - 1])):
                outln(mTree[comp - c - 1][q])

    else:
        if nivel == 0:
            for i in range(len(transacoes)):
                transacoesCode.append(one_hash(transacoes[i]))
            mTree.append(transacoesCode)
            transacoesCode = []
            nivel = +1

        for i in range(0, len(transacoes) - 1, 2):
            transacoesCode.append(sum_hash(transacoes[i], transacoes[i + 1]))
        mTree.append(transacoesCode)

        MerkleTree(transacoesCode)


if __name__ == "__main__":

    mTree = []
    nivel = 0
    n = int(readln())

    transacoes = geraTransacao(n)

    MerkleTree(transacoes)
