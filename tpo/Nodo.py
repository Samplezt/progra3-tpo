class Nodo:
    def __init__(self, name = " ", distance = 10000):
        self.name = name
        self.edges = []
        self.distance = distance
        self.visited = False

    def print_details(self):
        print(self.name)

    def add_edge(self, edge = None):
        self.edges.append(edge)
    
    def set_visited(self, b = True):
        self.visited = b
    
    def is_visited(self):
        return self.visited
    
    def get_name(self):
        return self.name
    
    def edge_list(self):
        return self.edges
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance