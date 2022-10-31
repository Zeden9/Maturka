myFile = open("Matura2023\szachy_przyklad.txt", "r")
game = myFile.readlines()

boards = []
for i in range(0, len(game), 9):
    board = []
    for j in range(0, 8):
        board.append(game[i+j])
    boards.append(board)

occupiedSpaces = []
for n in range(0, len(boards)):
    occupiedSpace = []
    for x in range(0,8):
        xPusty = False
        for y in range (0,8):
            if(boards[n][y][x] != "."):
                xPusty = True
        if(xPusty):
            occupiedSpace.append(x)
    occupiedSpaces.append(occupiedSpace)

clearCollumn = 0
mostClear = 0
for n in range(0, len(boards)):
    if(len(occupiedSpaces[n])<8):
        clearCollumn+=1
        if(8-len(occupiedSpaces[n]) > mostClear):
            mostClear = 8-len(occupiedSpaces[n])
    

# pieces = ['k', 'h', 's', 'g', 'w', 'p']
# cipka=0
# for board in boards:
#     pizda = True
#     board = ''.join(board)
#     for piece in pieces:
#         if board.count(piece) != board.count(piece.upper()):      a method from some guy - im jealous
#             pizda = False
#             break
#     if pizda:
#         cipka+=1
# print(cipka)

print(clearCollumn, mostClear)
piecesBlack = []
piecesWhite = []
for n in range(0, len(boards)):
    pieceBlack = []
    pieceWhite = []
    
    for x in range(0,8):
        for y in range (0,8):
            if(boards[n][y][x] != "."): 
                if(boards[n][y][x].isupper()):
                    pieceWhite.append(boards[n][y][x])
                    pieceWhite.sort()
                else:
                    pieceBlack.append(boards[n][y][x].upper())
                    pieceBlack.sort()
    piecesBlack.append(pieceBlack)
    piecesWhite.append(pieceWhite)

balancedBoards = 0
leastPiecesBalanced = 100
for n in range(0, len(boards)):
    if(piecesBlack[n] == piecesWhite[n]):
        balancedBoards+=1
        if(len(piecesWhite[n]*2) < leastPiecesBalanced):
            leastPiecesBalanced = len(piecesWhite[n]*2)



print(balancedBoards, leastPiecesBalanced)

