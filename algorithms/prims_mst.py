"""
Prim algorithm for finding Minimum Spanning Tree of weighted undirected graphs.
"""
import heapq
from collections import defaultdict

def prim_mst(num_nodes: int, edges: list):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))
    visited = set([0])
    pq = list(adj[0])
    heapq.heapify(pq)
    mst = []
    total_cost = 0
    while pq and len(visited) < num_nodes:
        w, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            total_cost += w
            for next_w, next_v in adj[v]:
                if next_v not in visited:
                    heapq.heappush(pq, (next_w, next_v))
    return total_cost
