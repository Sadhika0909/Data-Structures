class Graph:
    def __init__(self):
        self.graph={}
    def add(self,data):
        if data not in self.graph:
            self.graph[data]=[]
    def edge(self,node1,node2,directed=False):
        if node1 not in self.graph:
            self.add(node1)
        if node2 not in self.graph:
            self.add(node2)
        self.graph[node1].append(node2)
        if not directed:
            self.graph[node2].append(node1)
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

while True:
    if __name__=="__main__":
        graph=Graph()
        nb=int(input("\nNumber of items: "))
    while True:
        a=input("\nWhich function would you like to you use? Your options are: add, edge, display, delete_node, delete_edge, exit. ")
        if a=="add":
            for i in range(nb):
                node=input("What items would you like to add ")
                graph.add(node)
            print("Added node(s).")
        elif a=="edge":
            node1=input("Which is your first node? ")
            node2=input("Which is your second node? ")
            graph.edge(node1,node2,directed=True)
            print("Added edge.")
        elif a=="display":
            print("Graph: ")
            graph.display()
        elif a=="delete_node":
            n=input("Which node would you like to delete? ")
            graph.delete_node(n)
        elif a=="delete_edge":
            e=input("Which is your first node from the edge? ")
            e1=input("Which is your second node from the edge? ")
            graph.delete_edge(e,e1,directed=True)
        elif a=="exit":
            break
    break