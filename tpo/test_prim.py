# inicializmos el grafo

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
G = Nodo("G")
H = Nodo("H")
I = Nodo("I")


AB = Arista(A,B,4)
A.add_edge(AB)

AH = Arista(A,H,8)
A.add_edge(AH)

BH = Arista(B,H,11)
B.add_edge(BH)

BC = Arista(B,C,8)
B.add_edge(BC)

CD = Arista(C,D,7)
C.add_edge(CD)

CF = Arista(C,F,4)
C.add_edge(CF)

HI = Arista(H,I,7)
H.add_edge(HI)

HG = Arista(H,G,1)
H.add_edge(HG)

IC = Arista(I,C,2)
I.add_edge(IC)

IG = Arista(I,G,6)
I.add_edge(IG)

GF = Arista(G,F,2)
G.add_edge(GF)

DF = Arista(D,F,14)
D.add_edge(DF)

FD = Arista(F,D,14)
F.add_edge(FD)

DE = Arista(D,E,9)
D.add_edge(DE)

FE = Arista(F,E,10)
F.add_edge(FE)

grafo.add_node(A)
grafo.add_node(B)
grafo.add_node(C)
grafo.add_node(D)
grafo.add_node(E)
grafo.add_node(F)
grafo.add_node(G)
grafo.add_node(H)
grafo.add_node(I)

#grafo.prim(A)
grafo.bfs(A)
#grafo.dfs(A)