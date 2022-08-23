<h1 align="center">
     Arvores  </a>
</h1>

<h4 align="center">
	🚧   Concluido   🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
     * [Primeira parte](#primeira-parte)
        * [Testes](#testes-1)
     * [Segunda parte](#segunda-parte)
        * [Testes](#testes-2)
     * [Terceira parte](#terceira-parte)
        * [Testes](#testes-3)

<!--te-->


## 💻 Sobre o projeto

Este projeto tem como objetivo a consolidação dos conhecimentos sobre a estruturas
de dados estudadas em Algoritmos e Estruturas de Dados com foco na programação das estruturas, 
vantagens e desvantagens de cada uma, nomeadamente no que diz respeito a complexidade temporal e
espacial análise teórica e empírica da complexidade temporal.

O programa é dividido em três partes.

---
## Primeira parte

#### Merkle Tree para Integração numa Nova Criptomoeda

Uma Merkle Tree ou Hash Tree é uma estrutura usada em criptografia em que cada folha da
árvore é anotada com o hash code referente a um bloco de dados. Os nós internos são anotados
com o hash code dos seus filhos.
Estas árvores servem para fazer uma verificação segura do conteúdo de extensas estruturas de
dados. Vamos ainda assumir que a Hash Tree é formada a partir de uma árvore binária completa.
A figura abaixo apresenta uma Merkle Tree.

<img align="center" src="https://cdn.discordapp.com/attachments/773515424197115925/1011410578172035174/unknown.png"/>

Entrada:
Como entrada o programa recebe uma linha com o número de transações a codificar, seguida de uma linha
com as transações na forma BBBBddmmaaaa, separadas por espaço em branco, em que BBBB é um valor
0..9999, dd o dia 01..31, mm o mês 0..12, aa o ano 2007..2100. Sempre que os valores da dimensão tempo
forem menores que 10 devem ser precedidos de 0. A transação é guardada e tratada na forma de um long
integer.
O número de transações a codificar é uma potência de 2!
Saída:
Os valores de hash inscritos na Merkel Tree varrendo a árvore da raiz para as folhas e da esquerda para a
direita. Um valor por linha, terminando também a última linha por “\n”. Nos exemplos abaixo foi usado o
método public int hashCode() ... mas para que possamos ter uma função de hash igual para qualquer linguagem, devem usar a seguinte para um elemento

~~~
long hashcode(long x) {
return x % 1000000007;
}
~~~
e esta para dois elementos

~~~
long hashcode(long x, long y) {
int mod = 1000000007;
return ((x % mod) + (y % mod)) % mod;
}
~~~

---
### Testes 1

*input*
```
1
77706112012
```

*output*
```
706111473 // comentário: nível 1
```

*input*
```
4
1001092010 255501092010 99920032021 77706112012
```

*output*
```
128325015 // comentário: nível 1
502182228 // comentário: nível 2
626142794 // comentário: nível 2
1092003   // comentário: nível 3
501090225 // comentário: nível 3
920031328 // comentário: nível 3
706111473 // comentário: nível 3
```

*input*
```
8
1001092010 255501092010 99920032021 77706112012 231012021 44403122020 6601122015 333303032019
```

*output*
```
666610402 // comentário: nível 1
128325015 // comentário: nível 2
538285387 // comentário: nível 2
502182228 // comentário: nível 3
626142794 // comentário: nível 3
634133733 // comentário: nível 3
904151661 // comentário: nível 3
1092003   // comentário: nível 4
501090225 // comentário: nível 4
920031328 // comentário: nível 4
706111473 // comentário: nível 4
231012021 // comentário: nível 4
403121712 // comentário: nível 4
601121973 // comentário: nível 4
303029688 // comentário: nível 4
```


---
## Segunda parte

#### Sistema de Gestão de Vacinação

Pretende-se desenvolver um programa que guarda registos dos utentes da uma rede nacional de
vacinação. Cada registo compreende o número de utente seguido um conjunto de dados associados
de vacinação. Para cada utente é inicialmente criado um registo que depois vai ser acedido com
bastante frequência (muito mais consultas ao sistema do que inserções, seja para incluir novas
vacinações seja para verificar se o utente tem uma determinada vacina em dia).
As operações (comandos) possíveis sobre o Sistema de Vacinação são:
1. ACRESCENTA <numUtente> <vacina> <data limite>
Se ainda não existe um registo com < numUtente > cria esse registo. Se já existe verifica se a
<vacina> já existe e nesse caso atualiza <data limite>, se vacina ainda não existe acrescenta <vacina> e <data limite>. A data deve ser inserida no formato ddmmyyyy.
Terminada a inserção deve imprimir uma linha com “NOVO UTENTE CRIADO” se ainda não
existir o < numUtente > no sistema; “NOVA VACINA INSERIDA” se já existe numUtente mas
ainda não tem informação sobre essa vacina; “VACINA ATUALIZADA” se vacina já existe, caso
em que só atualiza data.
2. CONSULTA < numUtente >
Mostra todas as vacinas e datas limite associadas a < numUtente >. Vacinas apresentadas por ordem
alfabética. Termina com uma linha com a palavra “FIM”.
Se < numUtente > não está presente no sistema devolve uma linha com “NAO ENCONTRADO”.
3. LISTAGEM
Faz a listagem de todos os < numUtente > guardados e respetivas <vacinas> e <data limite> seguida
de linha com a palavra “FIM”. < numUtente > e <vacinas> por ordem crescente.
4. APAGA
Elimina todos os registos no sistema, de seguida imprime a linha com “LISTAGEM DE NOMES
APAGADA”
5. FIM
Termina a sequência de comandos com uma linha com a palavra “FIM”:


---
### Testes 2

*input*
```
APAGA
ACRESCENTA 12340 polio 20022025
ACRESCENTA 56700 covid 10082023
ACRESCENTA 88100 tuberculose 15122030
CONSULTA 56700
ACRESCENTA 56700 covid 10102024
ACRESCENTA 56700 papeira 12112026
LISTAGEM
APAGA
FIM
```

*output*
```
LISTAGEM DE NOMES APAGADA
NOVO UTENTE CRIADO
NOVO UTENTE CRIADO
NOVO UTENTE CRIADO
56700 covid 10082023
FIM
VACINA ATUALIZADA
NOVA VACINA INSERIDA
12340 polio 20022025
56700 covid 10102024 papeira 12112026
88100 tuberculose 15122030
FIM
LISTAGEM DE NOMES APAGADA
```

*input*
```
ACRESCENTA 23456 polio 20032023
CONSULTA 23456
APAGA
CONSULTA 23456
FIM
```

*output*
```
NOVO UTENTE CRIADO
23456 polio 20032023
FIM
LISTAGEM DE NOMES APAGADA
NAO ENCONTRADO
```

*input*
```
ACRESCENTA 234 polio 20122025
ACRESCENTA 123 zeneca 12122030
ACRESCENTA 234 abacus 12032026
ACRESCENTA 123 covid 2122026
ACRESCENTA 123 abacus 2122032
CONSULTA 123
LISTAGEM
APAGA
CONSULTA 123
FIM
```

*output*
```
NOVO UTENTE CRIADO
NOVO UTENTE CRIADO
NOVA VACINA INSERIDA
NOVA VACINA INSERIDA
NOVA VACINA INSERIDA
123 abacus 2122032 covid 2122026 zeneca 12122030
FIM
123 abacus 2122032 covid 2122026 zeneca 12122030
234 abacus 12032026 polio 20122025
FIM
LISTAGEM DE NOMES APAGADA
NAO ENCONTRADO
```

---
## Terceira parte

#### Sistema de Gestão de Clientes Preferenciais

Pretende-se desenvolver um programa que guarda o registo dos clientes de empresa, com a
particularidade de o acesso a estes dados ser bastante assimétrica – 90% dos acessos são feitos a
5% dos clientes.
As operações (comandos) possíveis sobre o Sistema de Gestão de Clientes são:
1. CLIENTE <nome> <morada> <volume de compras em euros>
Se ainda não existe um registo com <nome> cria esse registo. Se já existe devolve a mensagem
“CLIENTE JA EXISTENTE” e não faz nada no registo de clientes. Se insere um novo cliente termina com uma linha com a frase “NOVO CLIENTE INSERIDO”
O <nome> é composto por uma única palavra e a <morada> pela palavra Rua ou Avenida seguida
de uma única palavra. O <volume de compras em euros> é do tipo inteiro.
2. AQUISICAO <nome> <volume de compras em euros>
Adiciona <volume de compras em euros> ao valor anteriormente guardado. Termina com uma linha
com a frase “AQUISICAO INSERIDA”. SE <nome> não existe no sistema termina com a frase
“CLIENTE NAO REGISTADO”.
2. CONSULTA <nome>
Mostra os dados do cliente, a saber <nome> <morada> <volume de compras em euros> a que se
segue a linha “FIM”.
Se <nome> não existe no sistema termina com uma linha com a frase “CLIENTE NÃO
REGISTADO”.
3. LISTAGEM
Faz a listagem de todos os <nomes> guardados e respetivas <morada> <volume de compras em
euros>, um por linha. A listagem deve apresentar os clientes por ordem alfabética. Termina com
uma linha com a palavra “FIM”.
<nomes> apresentados por ordem alfabética.
4. APAGA
Elimina todos os registos no sistema. Imprime uma linha com “LISTAGEM DE CLIENTES
APAGADA”.
5. FIM
Termina a sequência de comandos.

---
### Testes 3

*input*
```
APAGA
CLIENTE Joao Rua Dourada 500
CLIENTE Rui Rua Verde 2000
CLIENTE Manuel Rua Cheia 30000
CONSULTA Rui
AQUISICAO Rui 100000
LISTAGEM
APAGA
FIM
```

*output*
```
LISTAGEM DE CLIENTES APAGADA
NOVO CLIENTE INSERIDO
NOVO CLIENTE INSERIDO
NOVO CLIENTE INSERIDO
Rui Rua Verde 2000
FIM
AQUISICAO INSERIDA
Joao Rua Dourada 500
Manuel Rua Cheia 30000
Rui Rua Verde 102000
FIM
LISTAGEM DE CLIENTES APAGADA
```

*input*
```
CLIENTE pedro rua torta 100
CLIENTE manuel rua verde 333
CLIENTE antonio rua amarela 2000
LISTAGEM
AQUISICAO pedro 2000
AQUISICAO jose 10
LISTAGEM
APAGA
LISTAGEM
CLIENTE manuel rua verde 20000
CONSULTA manuel
CONSULTA pedro
LISTAGEM
FIM
```

*output*
```
NOVO CLIENTE INSERIDO
NOVO CLIENTE INSERIDO
NOVO CLIENTE INSERIDO
antonio rua amarela 2000
manuel rua verde 333
pedro rua torta 100
FIM
AQUISICAO INSERIDA
CLIENTE NAO REGISTADO
antonio rua amarela 2000
manuel rua verde 333
pedro rua torta 2100
FIM
LISTAGEM DE CLIENTES APAGADA
FIM
NOVO CLIENTE INSERIDO
manuel rua verde 20000
FIM
CLIENTE NAO REGISTADO
manuel rua verde 20000
FIM
```
