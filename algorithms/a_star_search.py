"""
A* heuristic graph pathfinding search algorithm.
"""
import heapq
from typing import Dict, List, Tuple, Callable

def a_star(graph: Dict[str, List[Tuple[str, int]]], start: str, goal: str, h: Callable[[str], int]):
    pq = [(h(start), 0, start, [start])]
    visited = {}
    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr == goal: return path, g
        if curr in visited and visited[curr] <= g: continue
        visited[curr] = g
        for nxt, weight in graph.get(curr, []):
            cost = g + weight
            heapq.heappush(pq, (cost + h(nxt), cost, nxt, path + [nxt]))
    return None, float('inf')
