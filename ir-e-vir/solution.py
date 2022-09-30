
def no(e):
    return e-1

def depth(node_number, visited,uncheck=False):
    global matrix_adj
    global visited_nodes_complete
    global n_nodes
    visited.add(node_number)
    if uncheck:
       return     
    for i in range(n_nodes):
        is_neighboor = matrix_adj[node_number-1][i]
        if is_neighboor and (not (i+1) in visited):
            if (i+1) in visited_nodes_complete:
                uncheck = True
                for item in [i+1 for i in range(n_nodes)]:
                    visited.add(item)
            depth(i+1, visited, uncheck)
    

def check_conectivity_node(node):
    global n_nodes
    visited = set()
    depth(node,visited,uncheck=False)
    # print(visited)
    if len(visited) == n_nodes:
        return True
    return False

while True:
    try:
        n_nodes, n_edges = list(map(int,input().split())) 
        if n_nodes == 0:
            break  
        matrix_adj = [[0 for _ in range(n_nodes)]  for _ in range(n_nodes)]
        for i in range(n_edges):
            a, b, direction = list(map(int,input().split())) 
            matrix_adj[no(a)][no(b)] = 1  
            matrix_adj[no(b)][no(a)] = 1 if direction==2 else 0
        # print(matrix_adj)
        visited_nodes_complete = set() #os nós que alcançam todos os demais
        for node in range(n_nodes):
            if check_conectivity_node(node+1):
                visited_nodes_complete.add(node+1)
            else:
                break
        result = 1 if len(visited_nodes_complete) == n_nodes else 0
        print(result)
    except EOFError:
        break
    except ValueError:
        break