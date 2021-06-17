# Simple Tic-Tac-Toe


#### About

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. 
A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly.
Let’s program Tic-Tac-Toe and get playing!

#### Learning outcomes

After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch,
using functions, handling errors, and processing user input.

## Stage 1/5: 'Welcome to the battlefield!'

 **Topics learned:**

> Introduction to Python

> Overview of the basic program

> Multi-line programs


###### Objectives

Your first task in this project is to print the game grid in the console output. Use what you’ve learned about the print() function to print three lines, each containing three characters (X’s and O’s) to represent a game of tic-tac-toe where all fields of the grid have been filled in.

###### Example

The example below shows how your output might look:
```
X O X
O X O
X X O 
```

## Stage 2/5: 'The user is the gamemaster'

 **Topics learned:**

> PEP 8

> Comments

> Basic data types

> Variables

> Taking input


###### Objectives

In this stage, you will write a program that:
* Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only ```X```, ```O``` and ```_``` symbols.
* Outputs a line of dashes ```---------``` above and below the grid, adds a pipe ```|``` symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.

###### Example 1:
```
Enter cells: O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
```
###### Example 2:
```
Enter cells: OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
```
## Stage 3/5: 'What's up on the field?'

 **Topics learned:**

> Avoiding bad comments

> Naming variables

> Boolean logic

> Comparisons

> If statement

> Else statement

> Elif statement

> For loop

> List comprehension

> Nested lists

> IDE

> PyCharm basics

###### Objectives

In this stage, your program should:

1. Take a string entered by the user and print the game grid as in the previous stage.
2. Analyze the game state and print the result. Possible states: 
* ```Game not finished``` when neither side has three in a row but the grid still has empty cells.
* ```Draw``` when no side has a three in a row and the grid has no empty cells.
* ```X wins```when the grid has three X’s in a row.
* ```O wins```when the grid has three O’s in a row.
* ```Impossible``` when the grid has three X’s in a row as well as three O’s in a row,or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).

In this stage, we will assume that either X or O can start the game.
You can choose whether to use a space ``` ``` or underscore ```_``` to print empty cells.

## Stage 4/5: 'First move!'

 **Topics learned:**
 
> Quotes and multi-line strings

> Escape sequences

> Type casting

> Invoking a function

> Declaring a function

> Scopes

> Basic string methods

> Split and join

###### Objectives

The program should work as follows:
1. Get the 3x3 grid from the input as in the previous stages.
2. Output this 3x3 grid as in the previous stages.
3. Prompt the user to make a move.
4. The user should input 2 numbers that represent the cell where they want to place their X.(the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
5. Analyze user input and show messages in the following situations:
* ```This cell is occupied! Choose another one!``` if the cell is not empty.
* ```You should enter numbers!``` if the user enters non-numeric symbols in the coordinates input.
* ```Coordinates should be from 1 to 3!``` if the user enters coordinates outside the game grid.
6. Update the grid to include the user's move and print the updated grid to the console.
The program should also check the user’s input. If the input is unsuitable, the program should tell the user why their input was wrong, and prompt them to enter coordinates again.
To summarize, you need to output the game grid based on the first line of input, and then ask the user to enter a move. Keep asking until the user enters coordinates that represent an empty cell on the grid, update the grid to include that move, and then output it to the console. You should output the field only 2 times: once before the user’s move, and once after the user has entered a legal move.

## Stage 5/5: Fight!

 **Topics learned:**
 
> Program execution

> While loop

> Loop control statements

> Errors

> Any and all

###### Objectives
In this stage, you should write a program that:
1. Prints an empty grid at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
3. Ends the game when someone wins or there is a draw.
You need to output the final result at the end of the game.

###### Example:
```
---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```





