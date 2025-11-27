import heapq
from utils.graph import SearchResult

def astar_search(map_data, start, goal):
    """A* Search - combines actual cost and heuristic"""
    if start == goal:
        return SearchResult([start], 0, 0, "A*")
    
    frontier = [(map_data.heuristics[start], 0, start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        f_cost, g_cost, current_city, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_city == goal:
            return SearchResult(path, g_cost, nodes_expanded, "A*")
        
        if current_city in explored:
            continue
            
        explored.add(current_city)
        
        for neighbor, distance in map_data.graph[current_city]:
            if neighbor not in explored:
                new_g_cost = g_cost + distance
                new_f_cost = new_g_cost + map_data.heuristics[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_f_cost, new_g_cost, neighbor, new_path))
    
    return SearchResult([], float('inf'), nodes_expanded, "A*")