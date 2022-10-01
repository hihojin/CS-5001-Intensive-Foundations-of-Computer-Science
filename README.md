# Maze closest exit finder
# Connect Four
#### 2 major individual assignments I have done in Python
Maze-solver program and Connect Four game program involve user interaction by providing menu options to the user.


The major functionality in the Maze program was finding the shortest path to an exit which I implemented BFS search algorithm
so the first exit found is guaranteed to be the closest exit from the user's starting location (any valid starting point; if invalid, showed meaningful messages).

After finding the closest exit, I also made the program to show the actual shortest path on the maze to the user.
Maze program allows the user to create his/her own maze to play with and can read from various types of maze saved in .txt files (provided by instructor)

I handled the second case (reading from txt files) more in depth than expected work from instructors by handling the case where
user does not just use the provided maze txt files but creates their version of maze text file that is in a different format so
even if the first line of the user's txt file does not begin by specifying the width and length, the program can still know which line
to add and creates a maze.

ConnectFour game was written by following object-oriented programming in python.
I used data structures such as queue so player's turn can be switched every time the user puts a piece
in a valid position on game board and a stack so it can track the last piece added to the board and
when the user chooses an option to 'undo the last piece' it removes the piece and asks the user to choose his/her next decision from menu option.
ConnectFour program does not end the game until it meets the game over condition or the user selected the "quit" option from menu option.
Lastly, the program shows the winner or tells the user there is a tie.

I carefully wrote uniitest for each method in every program I built, left comments for clarity, and handled errors and showed meaningful messages to user.
