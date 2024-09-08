class Graph:
    #constructor
    def __init__(self):
        #initialising a graph using dictionary
        self.graph={}
    #adding a node to the graph
    def add(self,data):
        if data not in self.graph:
            self.graph[data]=[]
    def edge(self,node1,node2,directed=False):
        if node1 not in self.graph:
            self.graph.add(node1)
        if node2 not in self.graph:
            self.graph.add(node2)
            
