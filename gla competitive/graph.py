# graph transformation functions

# connected components
def component(graph, start):
    seen = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in seen:
            seen.add(v)
            stack.extend(graph[v] - seen)
    return seen
def connected_components(graph):
    """
    Return a list of connected components of graph.
    """
    components = []
    seen = set()
    for v in graph:
        if v not in seen:
            c = component(graph, v)
            components.append(c)
            seen.update(c)
    return components

# a b: Add the edges (a, b) to G
# k: Print the number of connected components in T(k, G)
def T(k, G):
    if k == 1:
        print(len(connected_components(G)))
    else:
        for a in G:
            for b in G[a]:
                G[a].remove(b)
                G[b].remove(a)
                T(k - 1, G)
                G[a].add(b)
                G[b].add(a)

def add_edge(G, a, b):
    G[a].add(b)
    G[b].add(a)

# main
if __name__ == '__main__':
    # read input
    N, M = map(int, input().split())
    G = {i: set() for i in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        add_edge(G, a, b)

    # solve
    T(3, G)

# Path: gla competitive\graph.py
# graph transformation functions

# 