import os
import time
from queue import PriorityQueue as queue
from dataclasses import dataclass, field

INSERTION = 5
DELETION = 6
SUBSTITUTION = 7

def check_triangle_validity():
    assert(INSERTION + DELETION - SUBSTITUTION > 0)

def calculate_distance(source: str, target: str, return_matrix: bool = False) -> int:
    matrix_size = len(target) * len(source)
    row_size = len(target)
    matrix = [0] * matrix_size
    matrix[0] = min(INSERTION + DELETION, 0 if source[0] == target[0] else SUBSTITUTION)
    for i in range(1, matrix_size):
        row = i // row_size
        col = i % row_size
        cost = 0 if source[row] == target[col] else SUBSTITUTION
        if row == 0:
            matrix[i] = min(INSERTION * (i + 1) + DELETION, matrix[i - 1] + INSERTION, cost + INSERTION * i)
        elif col == 0:
            matrix[i] = min(matrix[i - row_size] + DELETION, DELETION * (row + 1) + INSERTION, cost + DELETION * row)
        else:
            matrix[i] = min(matrix[i - row_size] + DELETION, matrix[i - 1] + INSERTION, cost + matrix[i - 1 - row_size])
    if return_matrix: return matrix
    return matrix[-1]

@dataclass(order=True)
class Cell:
    distance: int
    location: int=field(compare=False)

def calculate_distance_greedy(source: str, target: str, inspect: bool = False) -> int:
    matrix_size = len(target) * len(source)
    row_size = len(target)
    max_row = len(source)

    matrix = [None] * matrix_size
    cell_queue = queue()
    def add_cell(distance: int, location: int):

        if matrix[location] and matrix[location] <= distance:
            return

        cell_queue.put(Cell(distance, location))
        matrix[location] = distance

    cost_a = 0 if source[0] == target[1] else SUBSTITUTION # 0, 1
    cost_b = 0 if source[1] == target[0] else SUBSTITUTION # 1, 0
    cost_c = 0 if source[1] == target[1] else SUBSTITUTION # 1, 1

    zero_point = min(INSERTION + DELETION, 0 if source[0] == target[0] else SUBSTITUTION)
    zero_right = min(INSERTION * 2 + DELETION, zero_point + INSERTION, cost_a + INSERTION)
    zero_below = min(zero_point + DELETION, DELETION * 2 + INSERTION, cost_b + DELETION)
    zero_diag = min(zero_right + DELETION, zero_below + INSERTION, cost_c + zero_point)

    add_cell(zero_right, 1)
    add_cell(zero_below, row_size)
    add_cell(zero_diag, row_size + 1)

    while cell := cell_queue.get():
        
        row = cell.location // row_size
        col = cell.location % row_size
        # cost = 0 if source[row] == target[col] else SUBSTITUTION

        # if cell.location == matrix_size - 2:
        #     return cell.distance + INSERTION
        # if cell.location == matrix_size - row_size - 1:
        #     return cell.distance + DELETION
        # if cell.location == matrix_size - row_size - 2:
        #     cost = 0 if source[row + 1] == target[col + 1] else SUBSTITUTION
        #     return cell.distance + cost

        if inspect:
            print(f'{row + 1}, {col + 1} \t {cell.distance}')

        if cell.location == matrix_size - 1:
            return cell.distance

        if row == max_row - 1:
            add_cell(cell.distance + INSERTION, cell.location + 1)
        elif col == row_size - 1:
            add_cell(cell.distance + DELETION, cell.location + row_size)
        else:
            cost_r = 0 if source[row] == target[col + 1] else SUBSTITUTION
            cost_b = 0 if source[row + 1] == target[col] else SUBSTITUTION
            cost_d = 0 if source[row + 1] == target[col + 1] else SUBSTITUTION

            right = min(cell.distance + INSERTION, INSERTION * (col + 2) + DELETION, INSERTION * (col + 1) + cost_r) if row == 0 else cell.distance + INSERTION
            below = min(cell.distance + DELETION, DELETION * (row + 2) + INSERTION, DELETION * (row + 1) + cost_b) if col == 0 else cell.distance + DELETION

            add_cell(right, cell.location + 1) # right
            add_cell(below, cell.location + row_size) # below
            add_cell(cell.distance + cost_d, cell.location + row_size + 1) # diag        

if __name__=='__main__':
    check_triangle_validity()
    if 1: 
        # testing for 10 * 1000 samples
        dictionary = []
        samples = []

        main_directory = os.path.dirname(os.path.abspath(__file__))

        with (open(os.path.join(main_directory, 'leven_samples.txt'), 'rt') as lsf,
            open(os.path.join(main_directory, 'leven_test_samples.txt.'), 'rt') as ltsf):
            dictionary = [word.rstrip() for word in lsf.readlines()]
            samples = [word.rstrip() for word in ltsf.readlines()]
        
        for sample in samples:
            for comp in dictionary:
                start1 = time.time_ns()
                leven1 = calculate_distance(sample, comp)
                end1 = time.time_ns()
                start2 = time.time_ns()
                leven2 = calculate_distance_greedy(sample, comp)
                end2 = time.time_ns()
                print(f'regular: {(end1 - start1)//1000} us \t\t\t\t\t greedy: {(end2 - start2)//1000} us \t\t\t\t\t {leven1 == leven2}')
                assert(leven1 == leven2)
        
        print('done for 10 * 1000')
    if 0:
        # testing for error case - regular
        src = 'coexpire'
        tar = 'evictee'
        result = calculate_distance(src, tar, True)
        result_str = ''

        for i, cell in enumerate(result):
            if not i % len(tar):
                result_str += '\n'
            else:
                result_str += '\t'
            result_str += str(cell)
        print(result_str)
    if 0:
        # testing for error case - greedy
        src = 'coexpire'
        tar = 'opalesce'
        res = calculate_distance_greedy(src, tar, True)
        print(res)
