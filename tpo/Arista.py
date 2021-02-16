class Arista:
    def __init__(self, start, dest, weight = 1):
        self.start = start
        self.dest = dest
        self.weight = weight

    def print_details(self):
        print(self.start, self.dest, self.weight)
        
    def get_start(self):
        return self.start
    
    def get_dest(self):
        return self.dest
    
    def get_weight(self):
        return self.weight