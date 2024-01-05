from maze_gen import generate_maze
from maze_solver import find_path

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def main():
    while True:
        try:
            size = int(input("Enter the size of the maze: "))
            wall_percentage = int(input("Enter the wall percentage (0-100): "))
            
            maze = generate_maze(size, wall_percentage)
            
            print("\nGenerated Maze:")
            print_maze(maze)
            
            solved_maze = find_path([row[:] for row in maze])  # Clone maze for pathfinding
            if solved_maze:
                print("\nSolved Maze:")
                print_maze(solved_maze)
            else:
                print("\nNo path found.")
            
            choice = input("Options: (1)Print Path, (2)Generate Another Puzzle, (3)Exit: ").lower()
            if choice == '1':
                print("\nPath:")
                print_maze(solved_maze)
            elif choice == '2':
                continue
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
