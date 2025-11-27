"""
Robot Pathfinding Algorithms Comparison
A comprehensive implementation of BFS, DFS, UCS, Greedy, and A* Search
for robot navigation in 2D grids with obstacles.
"""

from algorithms.bfs_grid import bfs_grid_search
from algorithms.dfs_grid import dfs_grid_search
from algorithms.ucs_grid import ucs_grid_search
from algorithms.greedy_grid import greedy_grid_search
from algorithms.astar_grid import astar_grid_search
from utils.grid import GridMap
from utils.visualization import compare_grid_algorithms, visualize_grid_path

def main():
    """Main function to run all grid algorithms and compare results"""
    print("=" * 60)
    print("🤖 ROBOT PATHFINDING ALGORITHMS COMPARISON")
    print("=" * 60)
    
    # Create a grid with obstacles
    grid_map = GridMap()
    start = (0, 0)
    goal = (4, 4)
    
    print(f"📍 Finding path from {start} to {goal}")
    print("📦 Grid layout (X = obstacle, . = free cell):")
    grid_map.print_grid()
    print()
    
    # Compare all algorithms
    compare_grid_algorithms(grid_map, start, goal)
    
    # Visualize the best path
    print("\n" + "=" * 60)
    print("🛣️  VISUALIZING OPTIMAL PATH")
    print("=" * 60)
    
    # Use A* to find and visualize the optimal path
    result = astar_grid_search(grid_map, start, goal)
    visualize_grid_path(grid_map, result.path, start, goal)

if __name__ == "__main__":
    main()
