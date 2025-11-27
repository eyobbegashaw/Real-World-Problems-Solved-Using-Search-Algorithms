from algorithms.bfs import bfs_search
from algorithms.ucs import ucs_search
from algorithms.greedy import greedy_search
from algorithms.astar import astar_search
from algorithms.bidirectional import bidirectional_search

def compare_algorithms(map_data, start, goal):
    """Compare all search algorithms"""
    algorithms = [bfs_search, ucs_search, greedy_search, astar_search, bidirectional_search]
    
    results = []
    for algorithm in algorithms:
        result = algorithm(map_data, start, goal)
        results.append(result)
        print(result)
    
    print("\n" + "=" * 60)
    print("📊 COMPARATIVE ANALYSIS")
    print("=" * 60)
    
    optimal_cost = min(r.cost for r in results if r.cost != float('inf'))
    
    print(f"{'Algorithm':<15} {'Optimal':<8} {'Cost':<6} {'Nodes Expanded':<15} {'Efficiency'}")
    print("-" * 60)
    
    for result in results:
        is_optimal = "Yes" if result.cost == optimal_cost else "No"
        efficiency = f"{result.cost/result.nodes_expanded:.2f}" if result.nodes_expanded > 0 else "N/A"
        print(f"{result.algorithm_name:<15} {is_optimal:<8} {result.cost:<6} {result.nodes_expanded:<15} {efficiency}")

def analyze_algorithm_properties():
    """Analyze theoretical properties of each algorithm"""
    print("\n" + "=" * 60)
    print("🔍 ALGORITHM PROPERTIES")
    print("=" * 60)
    
    properties = {
        "BFS": {
            "Completeness": "Yes",
            "Optimality": "Yes (for uniform edge costs)",
            "Time Complexity": "O(b^d)",
            "Space Complexity": "O(b^d)",
            "Best Use Case": "When all steps have same cost"
        },
        "UCS": {
            "Completeness": "Yes", 
            "Optimality": "Yes",
            "Time Complexity": "O(b^(1+C*/ε))",
            "Space Complexity": "O(b^(1+C*/ε))",
            "Best Use Case": "Optimal path finding with different costs"
        },
        "Greedy": {
            "Completeness": "No (can get stuck in loops)",
            "Optimality": "No",
            "Time Complexity": "O(b^m)",
            "Space Complexity": "O(b^m)", 
            "Best Use Case": "Quick solutions when optimality not required"
        },
        "A*": {
            "Completeness": "Yes",
            "Optimality": "Yes (with admissible heuristic)",
            "Time Complexity": "Exponential (good with good heuristic)",
            "Space Complexity": "O(b^d)",
            "Best Use Case": "Optimal path finding with good heuristic"
        },
        "Bidirectional": {
            "Completeness": "Yes",
            "Optimality": "Yes (with UCS or BFS)",
            "Time Complexity": "O(b^(d/2))",
            "Space Complexity": "O(b^(d/2))",
            "Best Use Case": "When start and goal both known"
        }
    }
    
    for algo, props in properties.items():
        print(f"\n{algo}:")
        for prop, value in props.items():
            print(f"  {prop}: {value}")