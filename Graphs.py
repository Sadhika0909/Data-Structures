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
            self.add(node1)
        if node2 not in self.graph:
            self.add(node2)
        #add edge from node 1 to node 2:
        self.graph[node1].append(node2)
        if not directed:
            self.graph[node2].append(node1)
    #function to display the graph
    def display(self):
        for i in self.graph:
            print(f"{i}:{self.graph[i]}")
    def delete_node(self,node):
        if node in self.graph:
            for i in self.graph:
                if node in self.graph[i]:
                    self.graph[i].remove(node)
            del self.graph[node]
        else:
            print("Node doesn't exist.")
    def delete_edge(self,node1,node2,directed=False):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        else:
            print("The edge doesn't exist")
    
        
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

#deleting the edge
graph.delete_edge("s","a")
print("Graph after deleting s to a:")
graph.display()

#deleting the node
graph.delete_node("f")
print("Graph after deleting node f:")
graph.display()
