
from Grafo import Grafo
from Nodo import Nodo
from Arista import Arista

grafo = Grafo()

A = Nodo("A")
B = Nodo("B")
C = Nodo("C")
D = Nodo("D")
E = Nodo("E")
F = Nodo("F")


AB = Arista(A,B)
AC = Arista(A,C)
AD = Arista(A,D)
CE = Arista(C,E)
CF = Arista(C,F)
DF = Arista(D,F)



A.add_edge(AB)
A.add_edge(AC)
A.add_edge(AD)
C.add_edge(CE)
D.add_edge(CF)
F.add_edge(DF)


grafo.add_node(A)
grafo.add_node(B)
grafo.add_node(C)
grafo.add_node(D)
grafo.add_node(E)
grafo.add_node(F)



grafo.bfs(A)