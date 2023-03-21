from enum import Enum
from numpy import ndarray, loadtxt, copy
import matplotlib.pyplot as plt

MAP_NAME: str = "input.txt"
TEST_MAP_NAME: str = "test_input.txt"
#Authors: Jawdigué

class Path(Enum):
    WHITE = 0
    GREEN = 1
    INITIAL = 3
    END = 4


def read_initial_map(file_name: str) -> ndarray:
    initial_map = loadtxt(file_name, dtype=int)
    return initial_map


def check_path(path_list: list[int]):
    for path_number in path_list:
        print(Path(path_number).name)


def is_white(matrix: ndarray, x: int, y: int):
    return matrix[x, y] == 0


def is_green(matrix: ndarray, x: int, y: int):
    return matrix[x, y] == 1


def is_finished(matrix: ndarray, x: int, y: int):
    return matrix[x, y] == 4


def update_matrix(matrix: ndarray):
    new_matrix = copy(matrix)

    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):

            actual_matrix_value = matrix[row, column]

            upper_row = max(row - 1, 0)
            bottom_row = min(row + 2, matrix.shape[0])

            left_column = max(column - 1, 0)
            right_column = min(column + 2, matrix.shape[1])

            if is_white(matrix=matrix, x=row, y=column):
                green_adjacent = 0

                for adjacent_row in range(upper_row, bottom_row):
                    for adjacent_column in range(left_column, right_column):

                        if adjacent_column == column and adjacent_row == row:
                            continue
                        elif is_green(matrix=matrix, x=adjacent_row, y=adjacent_column):
                            green_adjacent += 1

                if 1 < green_adjacent < 5:
                    new_matrix[row, column] = 1

            elif is_green(matrix=matrix, x=row, y=column):
                green_adjacent = 0

                for adjacent_row in range(upper_row, bottom_row):
                    for adjacent_column in range(left_column, right_column):

                        if adjacent_column == column and adjacent_row == row:
                            continue
                        elif is_green(matrix=matrix, x=adjacent_row, y=adjacent_column):
                            green_adjacent += 1

                if not (3 < green_adjacent < 6):
                    new_matrix[row, column] = 0

    return new_matrix


def generate_map_image(matrix: ndarray):
    plt.imshow(
        matrix,
        cmap='viridis',
        interpolation='nearest'
    )
    plt.show()


#################################
# Transformar a matrix em uma matrix linear
# Encontrar o ID com base na linha e na coluna
# a linha sendo sempre vezes o len de uma linha
# Menos a coluna que vai ser vir de offset
#################################


if __name__ == '__main__':
    path_map = read_initial_map(file_name=MAP_NAME)

    current_map = path_map
    while True:
        generate_map_image(current_map)
        updated_matrix = update_matrix(current_map)
        current_map = updated_matrix

    # print(path_map)
    # for line in path_map:
    #     check_path(path_list=line)