import heapq
from utils.grid import GridSearchResult

def ucs_grid_search(grid_map, start, goal):
    """UCS for grid - finds shortest path considering move costs"""
    if start == goal:
        return GridSearchResult([start], 0, 0, "UCS Grid")
    
    # Each move costs 1
    frontier = [(0, start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        cost, current_pos, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_pos == goal:
            return GridSearchResult(path, cost, nodes_expanded, "UCS Grid")
        
        if current_pos in explored:
            continue
            
        explored.add(current_pos)
        
        for neighbor in grid_map.get_neighbors(*current_pos):
            if neighbor not in explored:
                new_cost = cost + 1  # Each move costs 1
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, neighbor, new_path))
    
    return GridSearchResult([], float('inf'), nodes_expanded, "UCS Grid")