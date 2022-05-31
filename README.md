# CS-5001-Intensive-Foundations-of-Computer-Science
#### 2 major individual assignments I have done in Python
Maze-solver program and Connect Four game program involve user interaction by providing menu options to the user.


The major functionality in the Maze program was finding the shortest path to an exit which I utilized BFS
so the first exit found is guaranteed to be the closest exit from the user's starting location.

After finding the closest exit, I also made the program to show the actual shortest path on the maze to the user.
Maze program allows the user to create his/her own maze to play with and can read from various types of maze saved in .txt files (provided by instructor)

I handled the second case (reading from txt files) more in depth than expected work from instructors by handling the case where
user does not just use the provided maze txt files but creates their version of maze text file that is in a different format so
even if the first line of the user's txt file does not begin by specifying the width and length the program can still know which line
to add and creates as a maze.

ConnectFour game was written by following object-oriented programming in python.
I used data structures such as queue so player's turn can be switched every time the user puts a piece
in a valid position on game board and a stack so it can track the last piece added to the board and
when the user chose an option to 'remove the last piece' on board it can remove the piece.

I have also practiced to write uniitest for testing, proper comments, and error handlings.
