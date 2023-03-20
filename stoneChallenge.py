import numpy as np
import matplotlib.pyplot as plt

# Lê o arquivo input.txt e transforma em uma matriz.
matrix = np.loadtxt("input.txt", dtype=int)

# Find the starting point and the destination point
start_point = np.argwhere(matrix == 3)[0] # [0,0]
end_point = np.argwhere(matrix == 4)[0] # [64 ,84]

# Define a function to check if a cell is white
def is_white(x, y, new_matrix):
    return new_matrix[x, y] == 0

# Define a function to check if a cell is green
def is_green(x, y, new_matrix):
    return new_matrix[x, y] == 1

# Define a function to update the matrix
def update_matrix(matrix):
    matrixToUpdate = np.copy(matrix) #Matriz passada a cada vez que get_next_move é chamada
    new_matrix = np.copy(matrix)
    for i in range(matrix.shape[0]): # for each row
        for j in range(matrix.shape[1]): # for each column on i row
            if is_white(i, j, matrixToUpdate): #if current cell is white
                nGreenAdjacent = 0 # reset green_adjacent number
                for x in range(max(i-1, 0), min(i+1, matrix.shape[0])): #loop trough the adjacent column Cells 
                    for y in range(max(j-1, 0), min(j+1, matrix.shape[1])): #loop through the adjacent rows cells
                        if is_green(x, y, matrixToUpdate):
                            nGreenAdjacent += 1
                if nGreenAdjacent > 1 and nGreenAdjacent < 5:
                    new_matrix[i, j] = 1
            elif is_green(i, j, matrixToUpdate):
                nGreenAdjacent = 0
                for x in range(max(i-1, 0), min(i+1, matrix.shape[0])):#loop trough the adjacent column Cells 
                    for y in range(max(j-1, 0), min(j+1, matrix.shape[1])): #loop through the adjacent rows cells
                        if is_green(x, y, matrixToUpdate):
                            nGreenAdjacent += 1
                if not(nGreenAdjacent > 3  and nGreenAdjacent < 6): # Test if cell remains green or turns white
                    new_matrix[i, j] = 0
    return new_matrix

# 1st - Define a function to get the next move
def get_next_move(matrix, current_position, end_position):
    x, y = current_position
    new_matrix = np.copy(matrix)
    updated_matrix = update_matrix(new_matrix)
    plt.imshow(updated_matrix, cmap='hot', interpolation='nearest')
    plt.show()
    return 1

# Iniciando do zero
current_position = start_point
moves = []
while current_position is not end_point: #ao chegar na posição final, não haverá current position
    next_move = get_next_move(matrix, current_position, end_point)
    if next_move is None:
        break
    #moves.append(next_move[0])
    #current_position = next_move[1]

# Write the output to a file
with open("output.txt", "w") as f:
    f.write(" ".join(moves))