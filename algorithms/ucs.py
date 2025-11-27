import heapq
from utils.graph import SearchResult

def ucs_search(map_data, start, goal):
    """Uniform Cost Search - finds shortest path in terms of actual distance"""
    if start == goal:
        return SearchResult([start], 0, 0, "UCS")
    
    frontier = [(0, start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        cost, current_city, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_city == goal:
            return SearchResult(path, cost, nodes_expanded, "UCS")
        
        if current_city in explored:
            continue
            
        explored.add(current_city)
        
        for neighbor, distance in map_data.graph[current_city]:
            if neighbor not in explored:
                new_cost = cost + distance
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, neighbor, new_path))
    
    return SearchResult([], float('inf'), nodes_expanded, "UCS")