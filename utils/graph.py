class RomaniaMap:
    """Romania city map with road connections and heuristic distances"""
    
    def __init__(self):
        # Graph representation: city -> [(neighbor, distance)]
        self.graph = {
            'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
            'Zerind': [('Arad', 75), ('Oradea', 71)],
            'Oradea': [('Zerind', 71), ('Sibiu', 151)],
            'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
            'Timisoara': [('Arad', 118), ('Lugoj', 111)],
            'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
            'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
            'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
            'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
            'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
            'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
            'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
            'Giurgiu': [('Bucharest', 90)],
            'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
            'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
            'Eforie': [('Hirsova', 86)],
            'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
            'Iasi': [('Vaslui', 92), ('Neamt', 87)],
            'Neamt': [('Iasi', 87)]
        }
        
        # Straight-line distances to Bucharest (heuristic)
        self.heuristics = {
            'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
            'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
            'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
            'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
            'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,
            'Zerind': 374
        }

class SearchResult:
    """Container for search algorithm results"""
    
    def __init__(self, path, cost, nodes_expanded, algorithm_name):
        self.path = path
        self.cost = cost
        self.nodes_expanded = nodes_expanded
        self.algorithm_name = algorithm_name
    
    def __str__(self):
        return f"{self.algorithm_name}: Path: {' -> '.join(self.path)}, Cost: {self.cost}, Nodes Expanded: {self.nodes_expanded}"

def calculate_path_cost(map_data, path):
    """Calculate total cost of a path"""
    cost = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        for neighbor, distance in map_data.graph[current_city]:
            if neighbor == next_city:
                cost += distance
                break
    return cost