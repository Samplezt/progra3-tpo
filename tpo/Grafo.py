from Nodo import Nodo


class Grafo:
    def __init__(self, name = " "):
        self.name = name
        self.nodes = []

    def add_node(self, vertex = None):
        self.nodes.append(vertex)

    def print_details(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def dfs(self, node):
        str = " | "
        stack = []
        
        node.set_visited(True)
        stack.append(node)
        
        while(len(stack) > 0):
            n = stack.pop()
            str += n.get_name() + " | "
            for e in n.edge_list():
                if(not e.get_dest().is_visited()):
                    stack.append(e.get_dest())
                    e.get_dest().set_visited()
                    
        print(str)
        
    def bfs(self, node):
        str = " | "
        queue = []
        
        node.set_visited(True)
        queue.insert(0, node)
        
        while(len(queue) > 0):
            n = queue.pop()
            str += n.get_name() + " | "
            for e in n.edge_list():
                if(not e.get_dest().is_visited()):
                    queue.insert(0, e.get_dest())
                    e.get_dest().set_visited()
                    
        print(str)
        
    def prim(self, node):
        l = []
        node.set_visited()
        for e in node.edge_list():
            if(not e.get_dest().is_visited()):
                l.append(e)
        
        while(len(l) > 0):
            m = l[0]
            for e in l:
                if(e.get_weight() < m.get_weight()):
                    m = e
                    
            l.remove(m)

            if(not m.get_dest().is_visited()):
                m.get_dest().set_visited()
                print(m.get_start().get_name() + " - " + m.get_dest().get_name())
                n = m.get_dest()
                for e in n.edge_list():
                    if(not e.get_dest().is_visited()):
                        l.append(e)

    def dijkstra(self, node):
        l = []
        node.set_visited()
        node.set_distance(0)
        l.append(node)
        
        while(len(l) > 0):
            n = l.pop(0)
            for ed in n.edge_list():
                if(ed.get_start().get_distance() + ed.get_weight() < ed.get_dest().get_distance()):
                    ed.get_dest().set_distance(ed.get_start().get_distance() + ed.get_weight())
                    
            min_dist = Nodo("Aux")
            for nd in self.nodes:
                if(not nd.is_visited() and min_dist.get_distance() > nd.get_distance()):
                    min_dist = nd
                    
            if(not min_dist.get_name() == "Aux"):
                min_dist.set_visited()
                l.append(min_dist)
        print(len(l))
    
    def kruskal(self):
        ed = []
        for node in self.nodes:
            for edge in node.edge_list():
                ed.append(edge)
        
        while(len(ed) > 0):
            m = ed[0]
            for edge in ed:
                if(edge.get_weight() < m.get_weight()):
                    m = edge
            ed.remove(m)
            if(not m.get_start().is_visited() or not m.get_dest().is_visited()):
                print(m.get_start().get_name() + " - " + m.get_dest().get_name())
                m.get_start().set_visited()
                m.get_dest().set_visited()