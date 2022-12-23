#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, or Reversi (https://en.wikipedia.org/wiki/Reversi), is a board game
played by two players, playing "disks" of different colors an 8x8 board.
Despite having relatively simple rules, Othello is a game of high strategic depth.
In this homework you will need to simulate a simplified version of othello,
called Dumbothello, in which each player can capture the opponent's disks
by playing a new disk on an adjacent empty cell.
The rules of Dumbothello are:
- each player has an associated color: white, black;
- the player with black is always the first to play;
- in turn, each player must place a disk of their color in such a way
  to capture one or more opponent's disks;
- capturing one or more opponent's disks means that the disk played by the
  player changes into the player's color all the directly adjacent opponent's disks,
  in any horizontal, vertical or diagonal direction;
- after playing one's own disk, the captured opponent's disks change
  their color, and become the same color as the player who just played;
- if the player who has the turn cannot add any disk on the board,
  the game ends. The player who has the higher number of disks on the board wins
  or a tie occurs if the number of disks of the two players is equal;
- the player who has the turn cannot add any disk if there is
  no way to capture any opponent's disks with any move, or if there are no
  more free cells on the board.

Write a function dumbothello(filename) that reads the configuration of the
board from the text file indicated by the string "filename" and,
following the rules of Dumbothello, recursively generates the complete game tree
of the possible evolutions of the game, such that each leaf of the tree
is a configuration from which no more moves can be made.

The initial configuration of the chessboard in the file is stored line by
line in the file: letter "B" identifies a black disk, a "W" a white disk,
and the character "." an empty cell. The letters are separated by one or
more spacing characters.

The dumbothello function will return a triple (a, b, c), where:
- a is the total number of evolutions ending in a black victory;
- b is the total number of evolutions ending in a white victory;
- c is the total number of evolutions ending in a tie.

For example, given as input a text file containing the board:
. . W W
. . B B
W W B B
W B B W

The function will return the triple:
(2, 16, 0)

NOTICE: the dumbotello function or some other function used by it must be recursive.

'''
def getBoard(filename):
    board = []
    with open(filename) as f:
        for line in f:
            board.append(line.split())
    return board


#define a function playGame that takes in a board (list of lists) and a color (string)

def copyBoard(board):
  newBoard = []
  for i in range(len(board)):
    newBoard.append([])
    for j in range(len(board[i])):
      newBoard[i].append(board[i][j])
  return newBoard

def playGame(board : list[list[str]], color : str):

  if color == "B":
    otherColor = "W"
  else:
    otherColor = "B"

  #check if there are any moves left
  moves = [] #this is a list of tuples that will contain the coordinates of all the possible moves
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == ".":
        #check if there are any disks of the opposite color in the 8 directions
        #if there are, add the coordinates to the list of moves. Use a try/except block to avoid index errors
        try:

          if i-1 >= 0 and board[i-1][j] == otherColor:
            moves.append((i,j))
          elif i+1 < len(board) and board[i+1][j] == otherColor:
            moves.append((i,j))
          elif j-1 >= 0 and board[i][j-1] == otherColor:
            moves.append((i,j))
          elif j+1 < len(board[i]) and board[i][j+1] == otherColor:
            moves.append((i,j))
          elif i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == otherColor:
            moves.append((i,j))
          elif i-1 >= 0 and j+1 < len(board[i]) and board[i-1][j+1] == otherColor:
            moves.append((i,j))
          elif i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] == otherColor:
            moves.append((i,j))
          elif i+1 < len(board) and j+1 < len(board[i]) and board[i+1][j+1] == otherColor:
            moves.append((i,j))
        except:
          pass

  #print (moves)

  if len(moves) == 0: #base case
    #check how many disks of each color are on the board
    blackDisks = 0
    whiteDisks = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == "B":
          blackDisks += 1
        elif board[i][j] == "W":
          whiteDisks += 1
    if blackDisks > whiteDisks:
      return [1,0,0]
    elif whiteDisks > blackDisks:
      return [0,1,0]
    else:
      return [0,0,1]

  
  globalResults = [0,0,0]

  for move in moves:
    i = move[0]
    j = move[1]
    newBoard = copyBoard(board)

    #eat the disks in the 8 directions
    if i-1 >= 0 and newBoard[i-1][j] == otherColor:
      newBoard[i-1][j] = color
    if i+1 < len(board) and newBoard[i+1][j] == otherColor:
      newBoard[i+1][j] = color
    if j-1 >= 0 and newBoard[i][j-1] == otherColor:
      newBoard[i][j-1] = color
    if j+1 < len(board[i]) and newBoard[i][j+1] == otherColor:
      newBoard[i][j+1] = color
    if i-1 >= 0 and j-1 >= 0 and newBoard[i-1][j-1] == otherColor:
      newBoard[i-1][j-1] = color
    if i-1 >= 0 and j+1 < len(board[i]) and newBoard[i-1][j+1] == otherColor:
      newBoard[i-1][j+1] = color
    if i+1 < len(board) and j-1 >= 0 and newBoard[i+1][j-1] == otherColor:
      newBoard[i+1][j-1] = color
    if i+1 < len(board) and j+1 < len(board[i]) and newBoard[i+1][j+1] == otherColor:
      newBoard[i+1][j+1] = color

    #place the disk
    newBoard[i][j] = color

    #call the function again
    results = playGame(newBoard, otherColor)
    globalResults[0] += results[0]
    globalResults[1] += results[1]
    globalResults[2] += results[2]

  return globalResults

    


  


    



      



        

  pass



def dumbothello(filename : str) -> tuple[int,int,int] :
    # your code goes here

    board = getBoard(filename)
    results = playGame(board, "B")
    return tuple(results)


    

if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
