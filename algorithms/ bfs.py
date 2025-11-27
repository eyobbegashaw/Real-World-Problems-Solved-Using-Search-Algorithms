from collections import deque
from utils.graph import SearchResult, calculate_path_cost

def bfs_search(map_data, start, goal):
    """Breadth-First Search - finds shortest path in terms of number of edges"""
    if start == goal:
        return SearchResult([start], 0, 0, "BFS")
    
    frontier = deque([(start, [start])])
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        current_city, path = frontier.popleft()
        nodes_expanded += 1
        
        if current_city in explored:
            continue
            
        explored.add(current_city)
        
        for neighbor, distance in map_data.graph[current_city]:
            if neighbor not in explored and neighbor not in [city for city, _ in frontier]:
                new_path = path + [neighbor]
                
                if neighbor == goal:
                    cost = calculate_path_cost(map_data, new_path)
                    return SearchResult(new_path, cost, nodes_expanded, "BFS")
                
                frontier.append((neighbor, new_path))
    
    return SearchResult([], float('inf'), nodes_expanded, "BFS")