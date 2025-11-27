import heapq
from utils.grid import GridSearchResult

def astar_grid_search(grid_map, start, goal):
    """A* Search for grid using Manhattan distance heuristic"""
    if start == goal:
        return GridSearchResult([start], 0, 0, "A* Grid")
    
    g_cost = 0
    h_cost = grid_map.manhattan_distance(start, goal)
    frontier = [(g_cost + h_cost, g_cost, start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        f_cost, g_cost, current_pos, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current_pos == goal:
            return GridSearchResult(path, g_cost, nodes_expanded, "A* Grid")
        
        if current_pos in explored:
            continue
            
        explored.add(current_pos)
        
        for neighbor in grid_map.get_neighbors(*current_pos):
            if neighbor not in explored:
                new_g_cost = g_cost + 1  # Each move costs 1
                new_h_cost = grid_map.manhattan_distance(neighbor, goal)
                new_f_cost = new_g_cost + new_h_cost
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_f_cost, new_g_cost, neighbor, new_path))
    
    return GridSearchResult([], float('inf'), nodes_expanded, "A* Grid")