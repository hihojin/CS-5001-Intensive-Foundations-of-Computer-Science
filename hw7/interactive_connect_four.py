"""
Hyojin Kwak
CS 5001
HW7 ConnectFour class interactive class
Getting user inputs here and managing user interactions
offering menu options to users and let the game play until
game over condition meets or the user wants to quit (included in menu
option)
"""


from connect_four import ConnectFour


def main():
    game = ConnectFour()

    while not game.is_game_over():
        print('Game Options: ')
        print('1. play - P')
        print('2. undo - U')
        print('3, quit - Q')
        print(game)
        answer = input('please choose from the game option (P/U/Q): ')
        answer = answer.upper()
        if answer == 'P':
            print('valid columns are between 0 and 6 (0 & 6 included)')
            column = int(input('Choose a column to add a piece: '))
            try:
                game.add_piece(column)
            except ValueError as ex:
                print(ex)

        elif answer == 'U':
            try:
                game.undo()
            except ValueError as ex:
                print(ex)

        elif answer == 'Q':
            print('Game Over')
            winner = game.get_winner()
            print('Winner is', winner)
            break

        elif answer != 'P' and answer != 'Q' and answer != 'U':
            print('please choose from the menu option')

    if game.is_game_over():
        print(game)
        print('Game Over')
        winner = game.get_winner()
        print('Winner is', winner)


if __name__ == '__main__':
    main()
