"""
Hyojin Kwak
CS 5001
2022/4/7
HW6 maze solver proggram
This is to test functions in maze_solver program

- function including user input(interaction) no test
- function with no return, no test
- if function returns, test
"""


import maze_solver


def test_read_maze_from_file():
    # testing if it can read from txt file and make a maze as a 2d list
    file = open('maze-barrier.txt', 'r')
    content = file.readlines()
    actual = maze_solver.read_maze_from_file(content)
    expected = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'E', 'X', 'X', 'X', 'X', 'X',
                'X']]
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)

    file = open('maze-just-walls.txt', 'r')
    content = file.readlines()
    actual = maze_solver.read_maze_from_file(content)
    expected = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'E', 'X', 'X', 'X', 'X', 'X',
                'X']]
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)

    file = open('maze-many-exits.txt', 'r')
    content = file.readlines()
    actual = maze_solver.read_maze_from_file(content)
    expected = [['X', 'X', 'X', 'X', 'X', 'X', 'E', 'X', 'X', 'X', 'X', 'X',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', ' ', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'X', ' ',
                'X'],
                ['E', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ',
                'E'],
                ['X', ' ', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'X', ' ',
                'X'],
                ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'E', 'X', 'X', 'X', 'X', 'X',
                'X']]
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)


def test_find_closest_exit():
    # 3 * 3 maze with exit.
    maze = [['X', 'X', 'X'], ['X', ' ', 'X'], ['X', 'E', 'X']]
    start_point = [1, 1]
    actual = maze_solver.find_closest_exit(maze, start_point)
    expected = 1
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)

    # 4*4 maze with no exit.
    maze = [['X', 'X', 'X', 'X'], ['X', ' ', ' ', 'X'], ['X', 'X', 'X', 'X']]
    start_point = [1, 1]
    actual = maze_solver.find_closest_exit(maze, start_point)
    expected = -1
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)


def test_checking_exit():
    maze = [['X', 'E', 'X', 'X'], ['E', 'E', ' ', 'X'], ['X', ' ', ' ', 'E']]
    actual = maze_solver.checking_exit(maze)
    expected = False
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)

    maze = [['X', 'E', 'X', 'X'], ['E', ' ', ' ', 'X'], ['X', ' ', ' ', 'E']]
    actual = maze_solver.checking_exit(maze)
    expected = True
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)

    maze = [['X', 'X', 'X', 'X'], ['X', ' ', ' ', 'X'], ['X', ' ', ' ', 'X']]
    actual = maze_solver.checking_exit(maze)
    expected = False
    if expected != actual:
        print('false')
        print('actual', actual)
        print('expected', expected)


def main():
    test_read_maze_from_file()
    test_find_closest_exit()
    test_checking_exit()


if __name__ == '__main__':
    main()
