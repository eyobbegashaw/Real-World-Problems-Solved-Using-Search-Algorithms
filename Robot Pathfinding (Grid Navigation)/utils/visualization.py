from algorithms.bfs_grid import bfs_grid_search
from algorithms.dfs_grid import dfs_grid_search
from algorithms.ucs_grid import ucs_grid_search
from algorithms.greedy_grid import greedy_grid_search
from algorithms.astar_grid import astar_grid_search

def compare_grid_algorithms(grid_map, start, goal):
    """Compare all grid search algorithms"""
    algorithms = [
        bfs_grid_search,
        dfs_grid_search, 
        ucs_grid_search,
        greedy_grid_search,
        astar_grid_search
    ]
    
    results = []
    print("🔍 ALGORITHM RESULTS:")
    print("-" * 60)
    
    for algorithm in algorithms:
        result = algorithm(grid_map, start, goal)
        results.append(result)
        print(result)
    
    # Comparative analysis
    print("\n📊 COMPARATIVE ANALYSIS:")
    print("=" * 60)
    
    optimal_cost = min(r.cost for r in results if r.cost != float('inf'))
    
    print(f"{'Algorithm':<12} {'Optimal':<8} {'Cost':<6} {'Nodes':<8} {'Path Length':<12}")
    print("-" * 60)
    
    for result in results:
        is_optimal = "Yes" if result.cost == optimal_cost else "No"
        path_length = len(result.path) if result.path else 0
        print(f"{result.algorithm_name:<12} {is_optimal:<8} {result.cost:<6} {result.nodes_expanded:<8} {path_length:<12}")

def visualize_grid_path(grid_map, path, start, goal):
    """Visualize the grid with the path"""
    if not path:
        print("❌ No path found!")
        return
    
    print("🛣️  Path Visualization:")
    print("S = Start, G = Goal, * = Path, X = Obstacle, . = Free")
    print("-" * 30)
    
    for y in range(grid_map.height):
        row = []
        for x in range(grid_map.width):
            pos = (x, y)
            if pos == start:
                row.append('S')
            elif pos == goal:
                row.append('G')
            elif pos in path:
                row.append('*')
            elif grid_map.grid[y][x] == 1:
                row.append('X')
            else:
                row.append('.')
        print(' '.join(row))
    
    print(f"\n📏 Path length: {len(path) - 1} moves")
    print(f"📍 Path: {' -> '.join([f'({x},{y})' for x, y in path])}")

def analyze_grid_algorithm_properties():
    """Analyze theoretical properties of grid search algorithms"""
    print("\n🔍 GRID ALGORITHM PROPERTIES:")
    print("=" * 60)
    
    properties = {
        "BFS Grid": {
            "Completeness": "Yes",
            "Optimality": "Yes (shortest moves)",
            "Time Complexity": "O(w*h)",
            "Space Complexity": "O(w*h)",
            "Best For": "Finding shortest path in moves"
        },
        "DFS Grid": {
            "Completeness": "Yes", 
            "Optimality": "No",
            "Time Complexity": "O(w*h)",
            "Space Complexity": "O(w*h)",
            "Best For": "Memory efficiency in large grids"
        },
        "UCS Grid": {
            "Completeness": "Yes",
            "Optimality": "Yes",
            "Time Complexity": "O(w*h log(w*h))",
            "Space Complexity": "O(w*h)",
            "Best For": "When moves have different costs"
        },
        "Greedy Grid": {
            "Completeness": "No (can get stuck)",
            "Optimality": "No", 
            "Time Complexity": "O(w*h log(w*h))",
            "Space Complexity": "O(w*h)",
            "Best For": "Quick solutions in open spaces"
        },
        "A* Grid": {
            "Completeness": "Yes",
            "Optimality": "Yes (with admissible heuristic)",
            "Time Complexity": "O(w*h log(w*h))", 
            "Space Complexity": "O(w*h)",
            "Best For": "Optimal path finding efficiently"
        }
    }
    
    for algo, props in properties.items():
        print(f"\n{algo}:")
        for prop, value in props.items():
            print(f"  {prop}: {value}")