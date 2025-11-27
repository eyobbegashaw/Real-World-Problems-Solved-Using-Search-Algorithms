import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.graph import RomaniaMap, calculate_path_cost
from algorithms.bfs import bfs_search
from algorithms.ucs import ucs_search
from algorithms.greedy import greedy_search
from algorithms.astar import astar_search
from algorithms.bidirectional import bidirectional_search

def run_tests():
    """Run comprehensive tests"""
    romania = RomaniaMap()
    
    print("🧪 RUNNING TESTS...")
    
    # Test 1: Same city
    result = ucs_search(romania, 'Arad', 'Arad')
    assert result.cost == 0, "Same city test failed"
    print("✅ Same city test passed")
    
    # Test 2: Direct connection
    result = ucs_search(romania, 'Arad', 'Zerind')
    assert result.cost == 75, "Direct connection test failed"
    print("✅ Direct connection test passed")
    
    # Test 3: All algorithms find valid paths
    algorithms = [bfs_search, ucs_search, greedy_search, astar_search, bidirectional_search]
    for algorithm in algorithms:
        result = algorithm(romania, 'Arad', 'Bucharest')
        assert result.cost != float('inf'), f"{result.algorithm_name} failed to find path"
        assert len(result.path) >= 2, f"{result.algorithm_name} returned invalid path"
        print(f"✅ {result.algorithm_name} valid path test passed")
    
    # Test 4: UCS and A* find optimal path
    ucs_result = ucs_search(romania, 'Arad', 'Bucharest')
    astar_result = astar_search(romania, 'Arad', 'Bucharest')
    assert ucs_result.cost == astar_result.cost == 418, "Optimality test failed"
    print("✅ UCS and A* optimality test passed")
    
    print("\n🎉 ALL TESTS PASSED!")

if __name__ == "__main__":
    run_tests()