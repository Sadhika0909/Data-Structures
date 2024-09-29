class Graph:
    #constructor function
    def __init__(self,v):
        self.v=v
        self.adj=[[]for i in range(v)]
    def dfsu(self,v,visited,temp):
        #marking the current vertex as visited
        visited[v]=True
        temp.append(v)
        print(v,end=" ")
        #loop through all adjacent vertices
        for i in self.adj[v]:
            #if adjacent vertex i is not visited, dfs is performed
            if not visited[i]:
                self.dfsu(i,visited,temp)
    def dfs(self,start_vertex):
        #marking all vertices as not visited
        visited=[False]*self.v
        print("DFS traversal starting from vertex",start_vertex,":")
        #calling the recursive function to perform DFS
        self.dfsu(start_vertex,visited)
        print()
    def bfs(self,start_vertex):
        #marking all the start vertices as not visited
        visited=[False]*self.v
        #creating an empty queue
        queue=[]
        #marking the vertex as visited and enqueuing it
        queue.append(start_vertex)
        visited[start_vertex]=True
        print("BFS traversal starting from vertex",start_vertex+":")
        while queue:
            v=queue.pop(0)
            print(v,end=" ")
            #getting all the adjacent vertices of the dequeued vertex v
            for i in self.adj[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
        print()
    #function to add un undirected edge between two vertices
    def undir(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    #function to find and return all connected components
    def connected(self):
        visited=[False]*self.v
        a=[]
        for i in range(self.v):
            if not visited[i]:
                temp=[]      
                self.dfsu(i,visited,temp) 
                a.append(temp) 
        return a
if __name__=="__main__":
    graph=Graph(7)
    graph.undir(0,1)
    graph.undir(2,3)
    graph.undir(4,5)
    graph.undir(5,6)
    b=graph.connected()
    print("Connected components: ")
    for i in b:
        print(i)
    #performing dfs
    graph.dfs(0)
    graph.bfs(0)
    
