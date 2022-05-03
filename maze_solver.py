"""
Hyojin Kwak
CS 5001
2022/4/7
HW6 maze solver proggram
This is a program that interacts with user by receiving width and height
of the maze, finding the shortest path from the starting point to the exit
Will keep user the menu options until the user wants to quit.
- width and height should be integers to draw a proper maze
- maze size should be at least 3
- 3 <= width <= 120 and 3<= height <= 40 height == lines, width == characters
- input should be all capital letters X (wall), E (exit), blank space == ' '
"""


import os


def read_maze_from_keyboard(width, height):
    """function: ask user to create a maze with given width and height
    which are also from the user input
    param: width, height, positive integers
    return: maze: list of list representing rows and cols"""
    maze = []
    counter_height = 0
    while counter_height < height:
        line = input('Please enter X for wall and E for exit in maze: ')
        line = line.upper().strip()
        if len(line) < width or len(line) > width:
            print('please try again')
            continue
        line = list(line)
        for i in line:
            should_add = True
            if i != 'X' and i != 'E' and i != ' ':
                should_add = False
                break
        if should_add:
            maze.append(line)
            counter_height += 1

    if checking_exit(maze):
        return maze
    print('maze not saved. at least 1 exit is required')


def read_maze_from_file(file_data):
    """funcction: reading text files and change
    string maze to a list of list maze for rows and cols
    representation
    param: list file_data
    return: maze: a list of lists representation"""
    maze = []
    if file_data[-1] == '\n':
        del file_data[-1]

    for i in range(len(file_data)):
        item = list(file_data[i].upper())
        item.remove('\n')
        for i in item:
            should_add = True
            if i != 'X' and i != 'E' and i != ' ':
                should_add = False
                break
        if should_add:
            maze.append(item)

    length = file_data[0].split()
    if checking_exit(maze):
        if 3 <= len(maze) <= 120 and 3 <= len(maze[0]) <= 40:
            if len(maze[0]) == int(length[0]) and len(maze) == int(length[1]):
                return maze
        else:
            print('maze not saved. wrong maze size')
    print('maze not saved. at least 1 exit is required')


def find_closest_exit(maze, start_point):
    """function: from the start point check its
    4 neighbors: up, down, left, right and determine if it
    is a valid move. If so we go to the neighbor cells and
    do the same process again until it reaches the exit. The first
    exit we find is guaranteed to be the shortest path/closest exit
    from the start point.
    param: start_point: list: [x, y], maze: list of lists
    return: shortest distance
    if no exit is found, return -1
    """
    # adding the current (x,y) to track the path
    start_point.append([(start_point[0], start_point[1])])
    # start point = [x, y, [current_location]]
    worklist = [start_point]
    # to store visited cells and if it's visited no need to search again
    visited = []
    # right (0, 1), down (1, 0), up (-1, 0), left (0, -1)
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while len(worklist) != 0:
        current = worklist.pop(0)
        for i in range(4):
            # check neighbors
            next_x = current[0] + dx[i]
            next_y = current[1] + dy[i]
            # the first exit it meets == the shortest exit
            if maze[next_x][next_y] == 'E':
                # current[2] == path
                for i in current[2]:
                    # in the path if it is not exit mark *
                    if maze[i[0]][i[1]] != 'E':
                        maze[i[0]][i[1]] = '*'
                # set startpoint to S
                maze[start_point[0]][start_point[1]] = 'S'
                # length of paths == shortest distance
                return len(current[2])
            if maze[next_x][next_y] == 'X':
                continue
            if next_x > len(maze) or next_y > len(maze[0]):
                continue
            neighbor = (next_x, next_y)
            if maze[next_x][next_y] == ' ' and neighbor not in visited:
                # if it is valid move, append the path
                path = current[2] + [neighbor]
                # append to the worklist so it can be popped next for search
                updated_current = [next_x, next_y, path]
                worklist.append(updated_current)
                # to avoid recheking neighbors of visited cells, append
                visited.append(neighbor)
    # if no exit found, return -1
    return -1


def print_maze(maze):
    """function: printing maze. If shortest path calculated
    print the maze with the stored path on the maze
    Param: maze: list of lists
    return: None"""
    try:
        for row in range(len(maze)):
            line = ''
            for col in range(len(maze[0])):
                line += maze[row][col]
            print(line)
    except TypeError:
        print('maze is not saved')


def checking_exit(maze):
    """Checking if exit exists in the boundary of maze
    param: maze (list of lists)
    return: return False if e not exist or e exist in elsewhere
    than the boundaries
    """
    for row in range(1, len(maze) - 1):
        for col in range(1, len(maze[0]) - 1):
            if 'E' in maze[row][col]:
                return False
    if 'E' in maze[0] or 'E' in maze[-1]:
        return True
    for col in range(len(maze)):
        if 'E' in maze[col][0] or 'E' in maze[col][-1]:
            return True
    else:
        return False


def main():
    """
    Showing the menu options until the user enters 5.
    (option to quit). The main function also handles error
    (exceptions). Calling appropriate function in each
    option following the user request.
    """
    print('!!!Welcome to the maze game!!!')

    while True:

        print('\n1. create your maze')
        print('2. bring maze template from file')
        print('3. get distance of the shortest path')
        print('4. print the maze to screen')
        print('5. exit the game')
        answer = input('\nEnter 1 or 2 or 3 or 4 or 5: ')
        if answer == "1":
            try:
                width = int(input('Please enter a width for your maze: '))
                height = int(input('Please enter a height for your maze: '))
                if width < 3:
                    print('\nwidth should be at least 3')
                elif height < 3:
                    print('\nheight should be at least 3')
                elif width > 120:
                    print('\nwidth should be at most 120')
                elif height > 40:
                    print('\nheight should be at most 40')
                else:
                    maze = read_maze_from_keyboard(width, height)

            # when floating values or string values -> value error gets printed
            except ValueError:
                print('invalid value that is not an integer value')

        elif answer == "2":
            filename = input('\nPlease enter the filename for your maze: ')
            try:
                if os.path.isdir(filename):
                    print('that is not a file. It is a directory')
                file = open(filename, 'r')
                file_data = file.readlines()
                maze = read_maze_from_file(file_data)
                file.close()

            except FileNotFoundError:
                print(filename, 'does not exist')
            except PermissionError:
                print('You do not have sufficient permissions to open',
                      filename)
            except OSError:
                print('An unexpected error occured while attempting to open',
                      filename)

        elif answer == "3":
            try:
                start_x = int(input('your x point: '))
                start_y = int(input('your y point: '))
                if start_x >= len(maze) or start_y >= len(maze[0]):
                    print('\nwidth and/or height is bigger than the maze size')
                elif start_x < 0 or start_y < 0:
                    print('should be greater than 0')
                else:
                    # checking if the startpoint is on the wall or at the exit
                    if maze[start_x][start_y] == 'X':
                        print('\nstarting point cannot be on the wall')
                        continue
                    # if start point is at exit, distance should be 0
                    elif maze[start_x][start_y] == 'E':
                        print('\ndistance is', 0)
                        continue
                    startpoint = [start_x, start_y]
                    distance = find_closest_exit(maze, startpoint)
                    if distance == -1:
                        print('\nno exit found')
                    else:
                        print('\ndistance is', distance)
                        print('\nto see the path in maze, choose 4')
            except ValueError:
                print('\nx, y should be integer values/ please write '
                      'x point first')
            except UnboundLocalError:
                print('\nplease choose option 1 or 2 first')

        elif answer == "4":
            try:
                print_maze(maze)
            except UnboundLocalError:
                print('\nplease choose option 1 or 2 first')

        elif answer == "5":
            print('bye!')
            break
        else:
            print('\nPlease enter 1 or 2 or 3 or 4 or 5')


if __name__ == '__main__':
    main()
