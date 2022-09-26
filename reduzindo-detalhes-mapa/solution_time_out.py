def by_weight(e):
    return e[2]

def no(e):
    return e-1

def depth(matrix_adj, node_number, visited, visited_map):
    global n_city
    visited.add(node_number)
    visited_map.append(node_number)
    for i in range(n_city):
        node_adj = matrix_adj[no(node_number)][i]
        if node_adj and (not (i+1) in visited):
            depth(matrix_adj, i+1, visited, visited_map) 
          
def is_connected(edge):
    visited = set()
    visited_map = []
    global n_city
    global matrix_adj
    k = 0
    for i in range(n_city):
        if (not (i+1) in visited):
            k = k + 1
            visited_map.append({k:[]})
            depth(matrix_adj,i+1,visited,visited_map[k-1][k])
    
    for component in range(k):
        if (edge[0] in visited_map[component][component+1]) and (edge[1] in visited_map[component][component+1]):
            return True
    
    return False

def get_sum(graph):
    total = 0
    for edge in graph:
        total += edge[2]
    return total

while True:
    try:
        n_city, m_street = list(map(int,input().split()))
        edge_list = []
        tree_kruskal = []
        matrix_adj = [[0 for _ in range(n_city)]  for _ in range(n_city)]
        for i in range(m_street):
            edge = list(map(int,input().split()))
            edge_list.append(edge) 
        edge_list.sort(key=by_weight)  
        for edge in edge_list:
            if not is_connected(edge):
                tree_kruskal.append(edge)
                matrix_adj[no(edge[0])][no(edge[1])] = 1
                matrix_adj[no(edge[1])][no(edge[0])] = 1
        print(get_sum(tree_kruskal))
    except EOFError:
        break
    except ValueError:
        break