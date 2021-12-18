class RollingRegistry:
    def __init__(self, size):
        self.registry_size = size
        self.registry = []
    
    def add(self, value):
        self.registry.append(value)
        if(len(self.registry) > self.registry_size):
            del self.registry[0]
        
        return self
    
    def last(self):
        if(len(self.registry) == 0):
            return None
        return self.registry[-1]
    
    def size(self):
        return len(self.registry)
    
    def average(self):
        if(len(self.registry) == 0):
            return 0
        return round(sum(self.registry) / len(self.registry), 1)
