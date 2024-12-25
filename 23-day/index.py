





data = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


connections = data.strip().splitlines()

from collections import defaultdict

# def calculate(connections):
#     graph = defaultdict(set)

#     for connection in connections:
#         a, b = connection.split('-')
#         graph[a].add(b)
#         graph[b].add(a)
#     total_t = 0
#     triangles = set()
#     for node in graph:
#         neighbors = graph[node]
#         for neighbor1 in neighbors:
#             for neighbor2 in neighbors:
#                 if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
#                     triangle = tuple(sorted([node, neighbor1, neighbor2]))
#                     triangles.add(triangle)
        
#     for triangle in triangles:
#         x, y, z = triangle
#         if x.startswith('t') or y.startswith('t') or z.startswith('t'):
#             total_t += 1
#     print(graph['ta'])
#     print(graph['qp'])
#     print(graph['ub'])
#     print(graph['tc'])
#     return graph


def calculate(connections):
    graph = defaultdict(set)

    for connection in connections:
        a, b = connection.split('-')
        graph[a].add(b)
        graph[b].add(a)
    total_t = 0
    triangles = set()
    # for node in graph:
    #     neighbors = graph[node]
    #     n = len(neighbors)
    #     subset = set()
    #     for i in range(n):
    #         neighbor1 = graph[neighbors[i]]
    #         for j in range(i+1, n):
    #             if neighbors[j] in graph[neighbor1]:
    #                 subset.add((neighbors[i], neighbors[j]))
    #     print(subset)

    



    return graph

            
def bron_kerbosch(graph, r=set(), p=None, x=set(), cliques=[]):
    # Bron-Kerbosch algorithm for finding cliques
    if p is None:
        p = set(graph.keys())
    
    if not p and not x:
        cliques.append(r)  # Found a clique
        return
    
    for node in list(p):
        bron_kerbosch(
            graph,
            r.union({node}),
            p.intersection(graph[node]),
            x.intersection(graph[node]),
            cliques
        )
        p.remove(node)
        x.add(node)

def largest_clique(graph):
    cliques = []
    bron_kerbosch(graph, cliques=cliques)
    # Find the largest clique
    max_clique = max(cliques, key=len)
    return sorted(max_clique)
graph = calculate(connections)
max_clique = largest_clique(graph)
password = ",".join(max_clique)
print("Password:", password)



