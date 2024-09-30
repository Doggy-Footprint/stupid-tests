import math
from queue import Queue as queue


INSERTION = 5
DELETION = 6
SUBSTITUTION = 7

def check_triangle_validity():
    assert(INSERTION + DELETION - SUBSTITUTION > 0)

def calculate_distance(source: str, target: str, use_greedy=False) -> int:
    if not use_greedy:
        row_size = len(target)
        matrix_size = len(target) * len(source)
        matrix = [0] * matrix_size
        for i in range(1, row_size):
            cost = 0 if source[0] == target[i] else SUBSTITUTION
            matrix[i] = min(INSERTION * (i + 1) + DELETION, matrix[i - 1] + INSERTION, cost + INSERTION * i)

        for i in range(row_size, matrix_size):
            cost = cost = 0 if source[i // row_size] == target[i % row_size] else SUBSTITUTION
            row = i // row_size
            if i % row_size == 0:
                matrix[i] = min(matrix[i - row_size] + DELETION, DELETION * (row + 1) + INSERTION, cost + DELETION * row)
            else:
                matrix[i] = min(matrix[i - row_size] + DELETION, matrix[i - 1] + INSERTION, cost + matrix[i - 1 - row_size])
        return matrix[-1]
    else:
        cell_queue = queue()
        
        

if __name__=='__main__':
    check_triangle_validity()
    result = calculate_distance('aacc', 'aabbcc')
    result_str = ''

    for i, cell in enumerate(result):
        if i % 6 == 0:
            result_str += '\n'
        else:
            result_str += '\t'
        result_str += str(cell)[:3]
    print(result_str)