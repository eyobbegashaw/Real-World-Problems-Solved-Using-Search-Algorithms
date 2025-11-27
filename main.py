"""
Route Planning Algorithms Comparison
A comprehensive implementation of BFS, UCS, Greedy, A*, and Bidirectional Search
for finding shortest paths in city networks.
"""

from algorithms.bfs import bfs_search
from algorithms.ucs import ucs_search
from algorithms.greedy import greedy_search
from algorithms.astar import astar_search
from algorithms.bidirectional import bidirectional_search
from utils.graph import RomaniaMap
from utils.visualization import compare_algorithms, analyze_algorithm_properties

def main():
    """Main function to run all algorithms and compare results"""
    print("=" * 60)
    print("🚀 ROUTE PLANNING ALGORITHMS COMPARISON")
    print("=" * 60)
    
    # Initialize the Romania map
    romania = RomaniaMap()
    start = 'Arad'
    goal = 'Bucharest'
    
    print(f"📍 Finding shortest path from {start} to {goal}\n")
    
    # Compare all algorithms
    compare_algorithms(romania, start, goal)
    
    # Show algorithm properties
    analyze_algorithm_properties()
    
    print("\n" + "=" * 60)
    print("✅ Comparison Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()