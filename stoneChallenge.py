import numpy as np
import matplotlib.pyplot as plt

# Lê o arquivo input.txt e transforma em uma matriz.
matrix = np.loadtxt("input.txt", dtype=int)

# Find the starting point and the destination point
start_point = np.argwhere(matrix == 3)[0] # [0,0]
end_point = np.argwhere(matrix == 4)[0] # [64 ,84]

# Define a function to check if a cell is white
def is_white(x, y):
    return matrix[x, y] == 0

# Define a function to check if a cell is green
def is_green(x, y):
    return matrix[x, y] == 1

# Define a function to update the matrix
def update_matrix(matrix):
    new_matrix = np.copy(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if is_white(i, j):
                green_adjacent = 0
                for x in range(max(i-1, 0), min(i+2, matrix.shape[0])):
                    for y in range(max(j-1, 0), min(j+2, matrix.shape[1])):
                        if is_green(x, y):
                            green_adjacent += 1
                if green_adjacent > 1 and green_adjacent < 5:
                    new_matrix[i, j] = 1
            elif is_green(i, j):
                green_adjacent = 0
                for x in range(max(i-1, 0), min(i+2, matrix.shape[0])):
                    for y in range(max(j-1, 0), min(j+2, matrix.shape[1])):
                        if is_green(x, y):
                            green_adjacent += 1
                if green_adjacent < 4 or green_adjacent > 5:
                    new_matrix[i, j] = 0
    return new_matrix

# 1st - Define a function to get the next move
def get_next_move(matrix, current_position, end_position):
    x, y = current_position
    if x == end_position[0] and y == end_position[1]:
        return None
    moves = []
    if x > 0 and is_white(x-1, y):
        moves.append(("U", (x-1, y)))
    if x < matrix.shape[0]-1 and is_white(x+1, y):
        moves.append(("D", (x+1, y)))
    if y > 0 and is_white(x, y-1):
        moves.append(("L", (x, y-1)))
    if y < matrix.shape[1]-1 and is_white(x, y+1):
        moves.append(("R", (x, y+1)))
    if not moves:
        return None
    moves_with_scores = []
    for move in moves:
        new_matrix = np.copy(matrix)
        new_matrix[x, y] = 1
        new_matrix[move[1]] = 3
        updated_matrix = update_matrix(new_matrix)
        plt.imshow(updated_matrix, cmap='hot', interpolation='nearest')
        plt.show()
        score = np.sum(updated_matrix == 1)
        moves_with_scores.append((score, move))
    moves_with_scores.sort(reverse=True)
    return moves_with_scores[0][1]

# Iniciando do zero
current_position = start_point
moves = []
while current_position is not None: #ao chegar na posição final, não haverá current position
    next_move = get_next_move(matrix, current_position, end_point)
    if next_move is None:
        break
    moves.append(next_move[0])
    current_position = next_move[1]

# Write the output to a file
with open("output.txt", "w") as f:
    f.write(" ".join(moves))
