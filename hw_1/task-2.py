from random import randint


def read_matrix():
    gen_matrix = []
    with open('input.txt') as file:
        lines = file.readlines()
        for line in lines:
            line_matrix = []
            for element in line.strip('\n').split(' '):
                line_matrix.append(int(element))
            gen_matrix.append(line_matrix)
    return gen_matrix


def create_random_matrix(size):
    random_matrix = []
    for index_x in range(size):
        line_list = []
        for index_y in range(size):
            line_list.append(randint(0, 100))
        random_matrix.append(line_list)
    return random_matrix


def find_num(num, matrix):
    column_index = []
    line_index = []
    for line_id in range(len(matrix)):
        for element_id in range(len(matrix[line_id])):
            if matrix[line_id][element_id] == num:
                line_index.append(line_id)
                column_index.append(element_id)
            else:
                continue
    return set(column_index), set(line_index)


using_matrix = int(input('Please, choose \n1. Use matrix from file - enter 1 \n2. Random matrix - enter 2 \n'))
if using_matrix == 1:
    task_matrix = read_matrix()
elif using_matrix == 2:
    matrix_size = int(input('Please, enter matrix size: '))
    task_matrix = create_random_matrix(matrix_size)
else:
    print('Wrong choice!! Used random martix 10x10')
    task_matrix = create_random_matrix(10)

print('Your matrix is:')
for rows in task_matrix:
    print(rows)

fined_num = int(input('Please, input integer value, that you want to found in matrix: \n'))

(find_in_col, find_in_row) = find_num(fined_num, task_matrix)

print(f'Number range:{fined_num} \nRows (index):{find_in_row} \nColumns (index):{find_in_col}')
