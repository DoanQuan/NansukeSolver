"""
* Nansuke solver  using pycosat.
- Author: Anh Quan
- Nansuke rules:
    + Each cell contains only one digit.
    + All sequence of digits must be appeared.
* Problem-solving (Encoding rules):
- Encoding the 1st rule: as Sudoku (??) compute index based on ... ??
- Encoding the 2nd rule: 2nd rule
"""

import pycosat
import os

max_range = 10

# nansuke_matrix = [
#     [0, 0, -1, -1, 0],
#     [-1, 0, 0, 0, 0],
#     [0, -1, 0, -1, 0],
#     [0, 0, 0, 0, -1],
#     [0, -1, -1, 0, 0]
# ]

# num_sequence = [
#     [1, 5],
#     [5, 1],
#     [1, 5, 3],
#     [1, 3, 5, 3],
#     [3, 5],
#     [5, 3],
#     [3, 1, 5],
#     [5, 3, 1, 5],
#     [5, 1, 3]
# ]

# nansuke_matrix = [
#     [-1, 0, -1, 0, 0],
#     [0, 0, 0, 0, -1],
#     [0, 0, -1, 0, 0],
#     [0, 0, 0, -1, 0],
#     [-1, -1, 0, 0, 0]
# ]
#
# num_sequence = [
#     [2, 0],
#     [2, 2],
#     [2, 4],
#     [4, 2],
#     [0, 2, 0],
#     [0, 2, 4],
#     [4, 0, 2],
#     [4, 2, 0],
#     [4, 2, 2],
#     [0, 0, 4, 2],
#     [4, 0, 2, 0]
# ]

# nansuke_matrix = [
#     [-1, -1, 0, -1, 0, -1, 0, -1],
#     [-1, 0, 0, 0, 0, 0, 0, -1],
#     [-1, -1, 0, -1, 0, -1, 0, -1],
#     [0, 0, 0, -1, 0, 0, 0, 0],
#     [-1, 0, 0, 0, 0, -1, -1, 0],
#     [0, 0, -1, 0, -1, -1, 0, 0],
#     [-1, 0, 0, 0, 0, 0, 0, -1],
#     [-1, 0, -1, 0, -1, -1, 0, 0]
# ]

# num_sequence = [
#     [4, 3, 2, 9, 8, 4],
#     [4, 4, 8, 2, 0, 1],
#     [4, 3, 2, 1, 7],
#     [6, 1, 3, 4, 3],
#     [7, 9, 8, 4, 8],
#     [1, 4, 1, 9],
#     [1, 7, 3, 8],
#     [3, 7, 8, 5],
#     [4, 0, 9, 6],
#     [6, 4, 3],
#     [8, 1, 3],
#     [8, 6, 1],
#     [1, 3],
#     [3, 2],
#     [8, 3]
# ]

nansuke_matrix = [
    [0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
    [-1, 0, -1, 0, 0, 0, 0, -1, 0, -1],
    [-1, 0, 0, -1, 0, -1, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, -1, 0, -1, 0],
    [0, -1, -1, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, -1, -1, 0],
    [0, -1, 0, -1, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, -1, 0, -1, 0, 0, -1],
    [-1, 0, -1, 0, 0, 0, 0, -1, 0, -1],
    [0, 0, 0, 0, -1, -1, 0, 0, 0, 0]
]

num_sequence = [
    [2, 1],
    [2, 6],
    [5, 2],
    [5, 3],
    [5, 4],
    [6, 2],
    [8, 5],
    [9, 7],
    [1, 3, 4],
    [1, 6, 2],
    [3, 1, 6],
    [4, 6, 5],
    [4, 9, 3],
    [5, 4, 8],
    [5, 6, 1],
    [7, 4, 2],
    [7, 5, 3],
    [7, 8, 3],
    [9, 4, 6],
    [9, 8, 3],
    [2, 4, 1, 8],
    [2, 4, 6, 9],
    [4, 6, 5, 2],
    [4, 8, 1, 2],
    [5, 1, 7, 4],
    [5, 9, 1, 8],
    [6, 7, 9, 3],
    [8, 3, 2, 7],
    [8, 4, 3, 7],
    [9, 5, 1, 2],
    [1, 6, 4, 3, 9],
    [2, 7, 6, 9, 4],
    [5, 7, 1, 2, 8],
    [7, 5, 4, 3, 1]
]

list_num = [

]

"""
list variable
    r_idx
    cl_idx
    len 
"""

R_IDX = "R_IDX"
CL_IDX = "CL_IDX"
VAR_LEN = "VAR_LEN"
DRT = "Direction"
ver = "Vertical"
point = "Point"
hor = "Horizontal"
list_var = [

]

list_cell_var = [

]

list_row_var = [

]

list_column_var = [

]

cell_var_count = 0
line_var_count = 0

start_row_index = 0
start_column_index = 0

cnf_matrix = []

matrix_size = 0


def get_cell_var_index(r, cl):
    for i in range(0, len(list_cell_var)):
        if r == list_cell_var[i][R_IDX] and cl == list_cell_var[i][CL_IDX]:
            return i

    return -1

def create_var_for_cell():
    for i in range(0, len(nansuke_matrix)):
        for j in range(0, len(nansuke_matrix[i])):
            if nansuke_matrix[i][j] == 0:
                list_cell_var.append({
                    R_IDX: i,
                    CL_IDX: j,
                    VAR_LEN: 1,
                    DRT: point
                })

def rotate_matrix(matrix):
    result_matrix = []
    for i in range(len(matrix[0])):
        matrix_line = []
        for j in range(len(matrix)):
            matrix_line.append(matrix[j][i])

        result_matrix.append(matrix_line)
    return result_matrix

def compute_var_len(matrix, row, column):
    res = 0
    for i in range(column, len(matrix[row])):
        if matrix[row][i] == 0:
            res += 1
        else:
            return res
    return res

def create_var_for_line():
    # Create line variable from input matrix
    for i in range(0, len(nansuke_matrix)):
        j = 0
        while j < len(nansuke_matrix[i]):
            if nansuke_matrix[i][j] == 0:
                var_len = compute_var_len(nansuke_matrix, i, j)
                if var_len > 1:
                    list_row_var.append({
                        R_IDX: i,
                        CL_IDX: j,
                        VAR_LEN: var_len,
                        DRT: hor
                    })
                    j += var_len
                else:
                    j += 1
            else:
                j += 1

    # Rotate inputted matrix and create line from rotated matrix
    rotated_matrix = rotate_matrix(nansuke_matrix)
    for i in range(len(rotated_matrix)):
        j = 0
        while j < len(rotated_matrix[i]):
            if rotated_matrix[i][j] == 0:
                var_len = compute_var_len(rotated_matrix, i, j)
                if var_len > 1:
                    list_column_var.append({
                        R_IDX: j,
                        CL_IDX: i,
                        VAR_LEN: var_len,
                        DRT: ver
                    })
                    j += var_len
                else:
                    j += 1
            else:
                j += 1

# Create list of variables used for generating cnf matrix
def create_list_variable():
    create_var_for_cell()
    create_var_for_line()

def encode_cell():
    # Each cell contains only one number
    # ALO for cells
    for i in range(0, len(list_cell_var)):
        cnf = []
        for j in range(0, max_range):
            cnf.append(i * max_range + j + 1)
        if len(cnf) > 0:
            cnf_matrix.append(cnf)

    # AMO for cells
    for i in range(0, len(list_cell_var)):
        for j in range(0, max_range):
            for k in range(j + 1, max_range):
                cnf_matrix.append([-1 * (i * max_range + j + 1),
                                  -1*(i * max_range + k + 1)])

def bind_row(row_idx, cnf_idx, seq_idx):
    r = list_row_var[row_idx][R_IDX]
    cl = list_row_var[row_idx][CL_IDX]

    for i in range(0, len(num_sequence[seq_idx])):
        var_id = get_cell_var_index(r, cl + i)
        cnf_matrix.append([-1*cnf_idx, var_id*max_range +
                           num_sequence[seq_idx][i] + 1])

def bind_column(cl_idx, cnf_idx, seq_idx):
    r = list_column_var[cl_idx][R_IDX]
    cl = list_column_var[cl_idx][CL_IDX]

    for i in range(0, len(num_sequence[seq_idx])):
        var_id = get_cell_var_index(r + i, cl)
        cnf_matrix.append([-1*cnf_idx, var_id*max_range +
                           num_sequence[seq_idx][i] + 1])

def encode_line():
    # ALO for each row
    for i in range(0, len(list_row_var)):
        cnf = []
        for j in range(0, len(num_sequence)):
            idx = start_row_index + i*len(num_sequence) + j + 1
            if list_row_var[i][VAR_LEN] == len(num_sequence[j]):
                cnf.append(idx)
                bind_row(i, idx, j)
            else:
                cnf_matrix.append([-1*idx])

        if len(cnf) > 0:
            cnf_matrix.append(cnf)

    # AMO for each row
    for i in range(0, len(list_row_var)):
        for j in range(0, len(num_sequence)):
            if list_row_var[i][VAR_LEN] == len(num_sequence[j]):
                for k in range(j + 1, len(num_sequence)):
                    if list_row_var[i][VAR_LEN] == len(num_sequence[k]):
                        arg_1 = start_row_index + i*len(num_sequence) + j + 1
                        arg_2 = start_row_index + i*len(num_sequence) + k + 1
                        cnf_matrix.append([-1*arg_1, -1*arg_2])

    # ALO for each column
    for i in range(0, len(list_column_var)):
        cnf = []
        for j in range(0, len(num_sequence)):
            idx = start_column_index + i*len(num_sequence) + j + 1
            if list_column_var[i][VAR_LEN] == len(num_sequence[j]):
                cnf.append(idx)
                bind_column(i, idx, j)
            else:
                cnf_matrix.append([-1*idx])

        if len(cnf) > 0:
            cnf_matrix.append(cnf)

    # AMO for each column
    for i in range(0, len(list_column_var)):
        for j in range(0, len(num_sequence)):
            if list_column_var[i][VAR_LEN] == len(num_sequence[j]):
                for k in range(j + 1, len(num_sequence)):
                    if list_column_var[i][VAR_LEN] == len(num_sequence[k]):
                        arg_1 = start_column_index + i*len(num_sequence) + j + 1
                        arg_2 = start_column_index + i*len(num_sequence) + k + 1
                        cnf_matrix.append([-1*arg_1, -1*arg_2])

    # All sequence of numbers must be appeared
    # ALO for a sequence
    for i in range(0, len(num_sequence)):
        cnf = []
        for j in range(0, len(list_row_var)):
            if list_row_var[j][VAR_LEN] == len(num_sequence[i]):
                idx = start_row_index + j*len(num_sequence) + i + 1
                cnf.append(idx)

        for j in range(0, len(list_column_var)):
            if list_column_var[j][VAR_LEN] == len(num_sequence[i]):
                idx = start_column_index + j*len(num_sequence) + i + 1
                cnf.append(idx)

        if len(cnf) > 0:
            cnf_matrix.append(cnf)

    # AMO for a sequence

def seq_can_fit(line, seq_num):
    print("can bind")
    if line[VAR_LEN] >= len(seq_num):
        return True

    return False

def encode_rules():
    encode_cell()
    encode_line()
    # bind_cell_with_line()

def list_has_value(list_value, value):
    for i in list_value:
        if i == value:
            return True

    return False

def get_list_var_for_cell():
    # Get list of numbers for each cell
    for i in num_sequence:
        for j in i:
            if not list_has_value(list_num, j):
                list_num.append(j)

    list_num.sort()


def main():
    global matrix_size
    global cell_var_count
    global line_var_count
    global start_row_index
    global start_column_index

    matrix_size = len(nansuke_matrix)

    get_list_var_for_cell()
    cell_var_count = len(list_num)
    line_var_count = len(num_sequence)

    create_list_variable()
    start_row_index = max_range * len(list_cell_var)
    start_column_index = start_row_index + line_var_count * len(list_row_var)

    encode_rules()
    for result in pycosat.itersolve(cnf_matrix):
        if result != "UNSAT":
            for i in range(0, len(list_cell_var) * max_range):
                if result[i] > 0:
                    idx = (result[i] - 1) // max_range
                    value = result[i] % max_range
                    if value == 0:
                        value = max_range
                    r = list_cell_var[idx][R_IDX]
                    cl = list_cell_var[idx][CL_IDX]
                    if value == 0:
                        print("hmm")
                    if idx == 6:
                        print("ss")
                    nansuke_matrix[r][cl] = value - 1
        for i in nansuke_matrix:
            print(i)
        print("\n\n")
    # result = pycosat.solve(cnf_matrix)
    # if result != "UNSAT":
    #     for i in range(0, len(list_cell_var) * max_range):
    #         if result[i] > 0:
    #             idx = result[i] // max_range
    #             value = result[i] % max_range
    #             r = list_cell_var[idx][R_IDX]
    #             cl = list_cell_var[idx][CL_IDX]
    #             nansuke_matrix[r][cl] = value - 1
    #
    #     for i in nansuke_matrix:
    #         print(i)

if __name__ == '__main__':
    main()
