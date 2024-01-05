from maze_gen import generate_maze
from maze_solver import find_path

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def main():
    while True:
        try:
            size = int(input("Enter the size of the maze (n * n): "))
            wall_percentage = size//2
            
            maze = generate_maze(size, wall_percentage)
            
            print("\nGenerated Maze:")
            print_maze(maze)
            
            solved_maze = find_path([row[:] for row in maze])  # Clone maze for pathfinding
            
            while True:
                choice = input("Options:\n1. Print the path \n2. Generate Another Puzzle \n3. Exit the game \nEnter your choice(1/2/3): ").lower()
                if choice == '1':
                    if solved_maze:
                        print("\nSolved Maze:")
                        print_maze(solved_maze)
                    else:
                        print("\nNo path found.")
                elif choice == '2':
                    break
                elif choice == '3':
                    print("Exiting the Game. Goodbye!")
                    return
                else:
                    print("Invalid option, Please try again.")

        except ValueError:
            print("Invalid input, Please enter a valid integer.")

if __name__ == "__main__":
    main()