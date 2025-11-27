import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.grid import GridMap
from algorithms.bfs_grid import bfs_grid_search
from algorithms.dfs_grid import dfs_grid_search
from algorithms.ucs_grid import ucs_grid_search
from algorithms.greedy_grid import greedy_grid_search
from algorithms.astar_grid import astar_grid_search

def run_grid_tests():
    """Run comprehensive grid algorithm tests"""
    grid_map = GridMap()
    
    print("🧪 RUNNING GRID ALGORITHM TESTS...")
    
    start = (0, 0)
    goal = (4, 4)
    
    # Test 1: All algorithms find valid paths
    algorithms = [bfs_grid_search, dfs_grid_search, ucs_grid_search, greedy_grid_search, astar_grid_search]
    
    for algorithm in algorithms:
        result = algorithm(grid_map, start, goal)
        assert result.cost != float('inf'), f"{result.algorithm_name} failed to find path"
        assert len(result.path) >= 2, f"{result.algorithm_name} returned invalid path"
        print(f"✅ {result.algorithm_name} test passed")
    
    # Test 2: BFS and UCS should find optimal path
    bfs_result = bfs_grid_search(grid_map, start, goal)
    ucs_result = ucs_grid_search(grid_map, start, goal)
    astar_result = astar_grid_search(grid_map, start, goal)
    
    assert bfs_result.cost == ucs_result.cost == astar_result.cost, "Optimality test failed"
    print("✅ BFS, UCS, A* optimality test passed")
    
    # Test 3: Direct neighbor path
    direct_result = bfs_grid_search(grid_map, (0, 0), (0, 1))
    assert direct_result.cost == 1, "Direct neighbor test failed"
    print("✅ Direct neighbor test passed")
    
    print("\n🎉 ALL GRID TESTS PASSED!")

if __name__ == "__main__":
    run_grid_tests()