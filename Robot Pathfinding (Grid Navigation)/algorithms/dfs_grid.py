from utils.grid import GridSearchResult

def dfs_grid_search(grid_map, start, goal):
    """DFS for grid - may not find shortest path"""
    if start == goal:
        return GridSearchResult([start], 0, 0, "DFS Grid")
    
    stack = [(start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while stack:
        current_pos, path = stack.pop()
        nodes_expanded += 1
        
        if current_pos in explored:
            continue
            
        if current_pos == goal:
            return GridSearchResult(path, len(path) - 1, nodes_expanded, "DFS Grid")
            
        explored.add(current_pos)
        
        # Reverse neighbors for consistent exploration order
        neighbors = grid_map.get_neighbors(*current_pos)
        for neighbor in reversed(neighbors):
            if neighbor not in explored:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    
    return GridSearchResult([], float('inf'), nodes_expanded, "DFS Grid")