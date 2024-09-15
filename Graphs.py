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
        #add edge from node 1 to node 2:
            self.graph(node2).append(node1)
    #function to display the graph
    def display(self):
        for i in self.graph:
            print(f"{i}:{self.graph[i]}")

graph=Graph()
graph.add("e")
graph.add("s")
graph.add("t")
graph.add("a")
graph.add("f")
graph.add("r")
graph.edge("e","s")
graph.edge("s","a")
graph.edge("s","f")
graph.edge("r","t")


graph.display()
