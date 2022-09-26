def by_weight(e):
    return e[2]

def no(e):
    return e-1

def get_sum(graph):
    total = 0
    for edge in graph:
        total += edge[2]
    return total

def find(x):
    global link
    while (x != link[no(x)]):
        x = link[no(x)]
    return x

def same(a, b):
    return find(a) == find(b)

def unite(a, b):
    global rank
    global link
    a = find(a)
    b = find(b)
    if (rank[no(a)] < rank[no(b)]):
        a, b = b, a
    rank[no(a)] += rank[no(b)]
    link[no(b)] = a


while True:
    try:
        n_city, m_street = list(map(int,input().split()))
        edge_list = []
        # tree_kruskal = []
        link = [ i+1 for i in range(n_city)]
        rank = [ 1 for i in range(n_city)]
        for i in range(m_street):
            edge = list(map(int,input().split()))
            edge_list.append(edge) 
        edge_list.sort(key=by_weight) 
        sum = 0 
        for edge in edge_list:
            if not same(edge[0], edge[1]):
                unite(edge[0], edge[1])
                #tree_kruskal.append(edge)
                sum += edge[2]
        print(sum)
    except EOFError:
        break
    except ValueError:
        break