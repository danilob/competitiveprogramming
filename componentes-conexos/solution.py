import string

def depth(matrix_adj, node_number, visited_map):
    global visited
    global number_letter_dict
    visited.add(number_letter_dict[node_number])
    visited_map.append(number_letter_dict[node_number])
    for i in range(len(number_letter_dict)):
        node_adj = matrix_adj[node_number][i]
        if node_adj and (not number_letter_dict[i] in visited):
            depth(matrix_adj, i, visited_map)

while True:
    try:
        cases = int(input())
        for case in range(cases):
            n_nodes, n_edges = list(map(int,input().split()))
            nodes = list(string.ascii_lowercase[:n_nodes])
            matrix_adj = [[0 for _ in range(n_nodes)]  for _ in range(n_nodes)]
            letter_number_dict = { letter:(ord(letter)-97) for letter in list(string.ascii_lowercase[:n_nodes]) }
            number_letter_dict = { (ord(letter)-97):letter for letter in list(string.ascii_lowercase[:n_nodes]) }
            edge_list = []
            for each_edge in range(n_edges):
                edge = input().split()
                edge_list.append(edge)
                matrix_adj[letter_number_dict[edge[0]]][letter_number_dict[edge[1]]] = 1
                matrix_adj[letter_number_dict[edge[1]]][letter_number_dict[edge[0]]] = 1
            visited = set()
            visited_map = []
            k = 0
            for i in range(n_nodes):
                if (not number_letter_dict[i] in visited):
                    k = k + 1
                    visited_map.append({k:[]})
                    depth(matrix_adj,i,visited_map[k-1][k])
            print(f'Case #{case+1}:')
            component = 1
            for item in visited_map:
                output = item[component]
                output.sort()
                print(','.join(output)+',')
                component += 1
            print(f'{len(visited_map)} connected components')        
            print()
            
    except EOFError:
        break
    except ValueError:
        break