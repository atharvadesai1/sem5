def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
        }
        return H_dist[n]
 
def astar(start,end):
    parent = {}
    open_set = set()
    closed_set = set()
    g={}
    g[start]= 0
    parent[start]=start
    open_set.add(start)
    
    while len(open_set)>0:
        n = None
        for v in open_set:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v    
        

        if n == end or Graph_nodes[n]==None:
            pass
        else:
            for (m,dist) in Graph_nodes[n]:
                if m not in open_set or m not in closed_set:
                    open_set.add(m)
                    parent[m]=n
                    g[m]=dist + g[n]
                else:
                    if g[m]>dist + g[n]:
                        g[m]=dist + g[n]
                        parent[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
                print('Path does not exist!')
                return None
        if n == end:
            print(parent)   
            path=[]

            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(start)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    return None
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
astar('A', 'G')