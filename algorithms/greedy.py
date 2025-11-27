import heapq
from utils.graph import SearchResult, calculate_path_cost

def greedy_search(map_data, start, goal):
    """Greedy Best-First Search - uses heuristic only"""
    if start == goal:
        return SearchResult([start], 0, 0, "Greedy")
    
    frontier = [(map_data.heuristics[start], start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        _, current_city, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_city == goal:
            cost = calculate_path_cost(map_data, path)
            return SearchResult(path, cost, nodes_expanded, "Greedy")
        
        if current_city in explored:
            continue
            
        explored.add(current_city)
        
        for neighbor, distance in map_data.graph[current_city]:
            if neighbor not in explored:
                new_path = path + [neighbor]
                heapq.heappush(frontier, (map_data.heuristics[neighbor], neighbor, new_path))
    
    return SearchResult([], float('inf'), nodes_expanded, "Greedy")