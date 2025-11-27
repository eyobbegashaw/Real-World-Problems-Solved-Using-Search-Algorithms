from collections import deque
from utils.graph import SearchResult, calculate_path_cost

def bidirectional_search(map_data, start, goal):
    """Bidirectional Search - searches from both start and goal simultaneously"""
    if start == goal:
        return SearchResult([start], 0, 0, "Bidirectional")
    
    forward_frontier = deque([(start, [start])])
    forward_explored = {start: [start]}
    
    backward_frontier = deque([(goal, [goal])])
    backward_explored = {goal: [goal]}
    
    nodes_expanded = 0
    
    while forward_frontier and backward_frontier:
        if forward_frontier:
            current_forward, forward_path = forward_frontier.popleft()
            nodes_expanded += 1
            
            if current_forward in backward_explored:
                backward_path = backward_explored[current_forward]
                full_path = forward_path + backward_path[-2::-1]
                cost = calculate_path_cost(map_data, full_path)
                return SearchResult(full_path, cost, nodes_expanded, "Bidirectional")
            
            for neighbor, distance in map_data.graph[current_forward]:
                if neighbor not in forward_explored:
                    new_path = forward_path + [neighbor]
                    forward_explored[neighbor] = new_path
                    forward_frontier.append((neighbor, new_path))
        
        if backward_frontier:
            current_backward, backward_path = backward_frontier.popleft()
            nodes_expanded += 1
            
            if current_backward in forward_explored:
                forward_path = forward_explored[current_backward]
                full_path = forward_path + backward_path[-2::-1]
                cost = calculate_path_cost(map_data, full_path)
                return SearchResult(full_path, cost, nodes_expanded, "Bidirectional")
            
            for neighbor, distance in map_data.graph[current_backward]:
                if neighbor not in backward_explored:
                    new_path = backward_path + [neighbor]
                    backward_explored[neighbor] = new_path
                    backward_frontier.append((neighbor, new_path))
    
    return SearchResult([], float('inf'), nodes_expanded, "Bidirectional")