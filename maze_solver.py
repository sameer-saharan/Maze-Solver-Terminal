import queue

# codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

def find_path(maze):
    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)
    
    visited = set()
    path = {}
    q = queue.Queue()
    q.put(start)
    visited.add(start)
    
    while not q.empty():
        current = q.get()
        x, y = current
        
        # Check if reached the end
        if current == end:
            break
        
        # Explore neighbors (up, down, left, right)
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != RED + '▓' + END_COLOR and (nx, ny) not in visited:
                q.put((nx, ny))
                visited.add((nx, ny))
                path[(nx, ny)] = current
    
    if end not in visited:
        return None
    
    # Reconstruct the path
    current = end
    while current != start:
        x, y = current
        maze[x][y] = GREEN + '◍' + END_COLOR  # Marking the path in green
        current = path[current]
    
    return maze