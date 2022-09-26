class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        sum = 0
        for u, v, weight in result:
            sum += weight
            
        return sum
 

while True:
    try:
        n_city, m_street = list(map(int,input().split()))
        edge_list = []
        tree_kruskal = []
        matrix_adj = [[0 for _ in range(n_city)]  for _ in range(n_city)]
        g = Graph(n_city)
        for i in range(m_street):
            edge = list(map(int,input().split()))
            g.add_edge(edge[0]-1,edge[1]-1,edge[2]) 
        print(g.kruskal())  
        
        # print(get_sum(tree_kruskal))
    except EOFError:
        break
    except ValueError:
        break 
