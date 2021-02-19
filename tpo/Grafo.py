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