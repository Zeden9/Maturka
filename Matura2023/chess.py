import os

myFile = open("Matura2023\szachy.txt", "r")
game = myFile.readlines()

board = []
for i in range(0, len(game), 9):
    step = []
    for j in range(0, 8):
        step.append(game[i+j])
    board.append(step)    

print(board[5])