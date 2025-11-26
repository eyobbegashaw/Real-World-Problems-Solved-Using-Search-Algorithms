# Real-World Problems Solved Using Search Algorithms

This repository demonstrates practical applications of various search algorithms across 8 different problem domains. Each implementation includes analysis of time and space complexity.

## Problems Covered

1. **City Map Navigation** - Route planning using BFS, UCS, Greedy, A*, and Bidirectional Search
2. **Robot Pathfinding** - Grid navigation with BFS, DFS, and A*
3. **8-Puzzle Solver** - Sliding puzzle solution with BFS and A* (Misplaced/Manhattan)
4. **Web Crawler Simulation** - Web page discovery using BFS, DFS, and DLS
5. **Social Network Connection Finder** - Friend connections via BFS and Bidirectional Search
6. **Network Packet Routing** - Optimal routing with UCS and A*
7. **Game AI Pathfinding** - Maze navigation using DFS, Greedy, and A*
8. **Word Ladder** - Word transformation with BFS, A*, and Bidirectional Search

## Algorithm Comparison

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity | Best Use Case |
|-----------|--------------|------------|-----------------|------------------|---------------|
| BFS | Yes | Yes | O(b^d) | O(b^d) | Shortest path problems |
| DFS | No | No | O(b^m) | O(bm) | Memory-constrained problems |
| UCS | Yes | Yes | O(b^(1+⌊C*/ε⌋)) | O(b^(1+⌊C*/ε⌋)) | Cost-sensitive routing |
| Greedy | No | No | O(b^m) | O(b^m) | Quick solutions with heuristic |
| A* | Yes | Yes* | O(b^d) | O(b^d) | Optimal pathfinding with heuristic |
| Bidirectional | Yes | Yes | O(b^(d/2)) | O(b^(d/2)) | Large search spaces |

*Optimal with admissible heuristic

## Installation

```bash
git clone https://github.com/eyobbegashaw/Real-World-Problems-Search-Algorithms.git
cd Real-World-Problems-Search-Algorithms
pip install -r requirements.txt
