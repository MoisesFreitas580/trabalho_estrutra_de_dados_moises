from listas_encadeadas_duplas import ListaEncadeadaDupla
from pilha import Pilha
from fila import Fila

print("-"*10+"Lista Encadeadas Dulpla"+"-"*10)
lista1 = ListaEncadeadaDupla()
lista1.printList()
lista1.append(3)
lista1.append(2)
lista1.append(7)
lista1.append(1)
lista1.printList()
lista1.removerNoInicio()
lista1.printList()
lista1.removerNoFinal()
lista1.printList()
lista1.inserirNoInicio(1)
lista1.printList()
lista1.inserirNoFinal(3)
lista1.printList()
lista1.removerItemDaLista(7)
lista1.printList()
lista1.buscarItem(3)

print("-"*10+"Pilha"+"-"*10)

pilha1 = Pilha(5)
pilha1.addTop(2)
pilha1.addTop('a')
pilha1.addTop(1)
pilha1.addTop(8)
pilha1.addTop([])
print(pilha1)
pilha1.addTop(9)
pilha1.removeTop()
pilha1.removeTop()
print(pilha1)

print("-"*10+"Fila"+"-"*10)

fila1 = Fila(5)

fila1.addStart(1)
fila1.addStart(2)
fila1.addStart(3)
fila1.addStart(4)
fila1.addStart(5)
print(fila1)
fila1.removeStart()
fila1.removeStart()
print(fila1)