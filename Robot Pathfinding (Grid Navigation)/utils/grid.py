class GridMap:
    """2D grid map for robot navigation with obstacles"""
    
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        
        # 0 = free cell, 1 = obstacle
        self.grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        
        # Movement directions: up, down, left, right
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-connected
        # For 8-connected: add diagonals: [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    def is_valid(self, x, y):
        """Check if cell is within grid bounds and not blocked"""
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                self.grid[y][x] == 0)
    
    def get_neighbors(self, x, y):
        """Get valid neighboring cells"""
        neighbors = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
    
    def print_grid(self):
        """Print the grid with obstacles"""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    row.append('X')  # Obstacle
                else:
                    row.append('.')  # Free cell
            print(' '.join(row))
    
    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions"""
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def euclidean_distance(self, pos1, pos2):
        """Calculate Euclidean distance between two positions"""
        x1, y1 = pos1
        x2, y2 = pos2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

class GridSearchResult:
    """Container for grid search algorithm results"""
    
    def __init__(self, path, cost, nodes_expanded, algorithm_name):
        self.path = path
        self.cost = cost
        self.nodes_expanded = nodes_expanded
        self.algorithm_name = algorithm_name
    
    def __str__(self):
        path_str = ' -> '.join([f"({x},{y})" for x, y in self.path])
        return f"{self.algorithm_name}: Path: {path_str}, Cost: {self.cost}, Nodes Expanded: {self.nodes_expanded}"