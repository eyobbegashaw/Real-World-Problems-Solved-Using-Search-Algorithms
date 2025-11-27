import heapq
from utils.grid import GridSearchResult

def greedy_grid_search(grid_map, start, goal):
    """Greedy Best-First Search for grid using Manhattan distance"""
    if start == goal:
        return GridSearchResult([start], 0, 0, "Greedy Grid")
    
    frontier = [(grid_map.manhattan_distance(start, goal), start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        _, current_pos, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_pos == goal:
            return GridSearchResult(path, len(path) - 1, nodes_expanded, "Greedy Grid")
        
        if current_pos in explored:
            continue
            
        explored.add(current_pos)
        
        for neighbor in grid_map.get_neighbors(*current_pos):
            if neighbor not in explored:
                new_path = path + [neighbor]
                heuristic = grid_map.manhattan_distance(neighbor, goal)
                heapq.heappush(frontier, (heuristic, neighbor, new_path))
    
    return GridSearchResult([], float('inf'), nodes_expanded, "Greedy Grid")