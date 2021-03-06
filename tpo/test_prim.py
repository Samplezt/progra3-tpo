
from Grafo import Grafo
from Nodo import Nodo
from Arista import Arista

grafo = Grafo()

A = Nodo("A")
B = Nodo("B")
C = Nodo("C")
D = Nodo("D")
E = Nodo("E")


AB = Arista(A,B,2)
AC = Arista(A,C,5)
AE = Arista(A,E,6)
BC = Arista(B,C,5)
BD = Arista(B,D,3)
BE = Arista(B,E,2)
EC = Arista(E,C,4)
DE = Arista(D,E,4)


A.add_edge(AB)
A.add_edge(AC)
A.add_edge(AE)

B.add_edge(BD)
B.add_edge(BE)
B.add_edge(BC)


E.add_edge(EC)
D.add_edge(DE)



grafo.add_node(A)
grafo.add_node(B)
grafo.add_node(C)
grafo.add_node(D)
grafo.add_node(E)


grafo.prim(A)