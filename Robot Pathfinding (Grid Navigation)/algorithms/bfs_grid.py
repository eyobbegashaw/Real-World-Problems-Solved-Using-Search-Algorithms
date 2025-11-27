from collections import deque
from utils.grid import GridSearchResult

def bfs_grid_search(grid_map, start, goal):
    """BFS for grid - finds shortest path in terms of number of moves"""
    if start == goal:
        return GridSearchResult([start], 0, 0, "BFS Grid")
    
    frontier = deque([(start, [start])])
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        current_pos, path = frontier.popleft()
        nodes_expanded += 1
        
        if current_pos in explored:
            continue
            
        explored.add(current_pos)
        
        for neighbor in grid_map.get_neighbors(*current_pos):
            if neighbor not in explored and neighbor not in [pos for pos, _ in frontier]:
                new_path = path + [neighbor]
                
                if neighbor == goal:
                    return GridSearchResult(new_path, len(new_path) - 1, nodes_expanded, "BFS Grid")
                
                frontier.append((neighbor, new_path))
    
    return GridSearchResult([], float('inf'), nodes_expanded, "BFS Grid")