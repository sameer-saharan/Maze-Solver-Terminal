import random

def generate_maze(size, wall_percentage):
    maze = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Set walls based on the specified percentage
    num_walls = int(size * size * wall_percentage / 100)
    for _ in range(num_walls):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        maze[x][y] = '▓'  # Wall
    
    # Set start and end positions
    maze[0][0] = 'S'
    maze[size-1][size-1] = 'E'
    
    # Set a different symbol for open spaces
    for i in range(size):
        for j in range(size):
            if maze[i][j] == ' ':
                maze[i][j] = '◌'  # Open Space
    
    return maze