class Node:
    def __init__(self, name):
        self.name = name
        self.friends = set()
    
    def add(self, *nodes):
        for n in nodes:
            self.friends.add(n)
            n.friends.add(self)
        return self

    def __str__(self):
        return self.name
