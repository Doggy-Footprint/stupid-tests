from queue import PriorityQueue as queue
from dataclasses import dataclass, field

INSERTION = 5
DELETION = 6
SUBSTITUTION = 7

def check_triangle_validity():
    assert(INSERTION + DELETION - SUBSTITUTION > 0)

def calculate_distance(source: str, target: str) -> int:
    matrix_size = len(target) * len(source)
    row_size = len(target)
    matrix = [0] * matrix_size
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
    return matrix[-1]

@dataclass(order=True)
class Cell:
    distance: int
    location: int=field(compare=False)

def calculate_distance_greedy(source: str, target: str) -> int:
    matrix_size = len(target) * len(source)
    row_size = len(target)
    max_row = len(source)

    cost_a = 0 if source[0] == target[1] else SUBSTITUTION # 0, 1
    cost_b = 0 if source[1] == target[0] else SUBSTITUTION # 1, 0
    cost_c = 0 if source[1] == target[1] else SUBSTITUTION # 1, 1

    zero_point = 0
    zero_right = min(INSERTION * 2 + DELETION, zero_point + INSERTION, cost_a + INSERTION + 1)
    zero_below = min(zero_point + DELETION, DELETION * 2 + INSERTION, cost_b + DELETION)
    zero_diag = min(zero_right + DELETION, zero_below + INSERTION, cost_c + zero_point)

    cell_queue = queue()
    cell_queue.put(Cell(zero_right, 1))
    cell_queue.put(Cell(zero_below, row_size))
    cell_queue.put(Cell(zero_diag, row_size + 1))

    while True:
        cell = cell_queue.get()
        
        row = cell.location // row_size
        col = cell.location % row_size
        # cost = 0 if source[row] == target[col] else SUBSTITUTION

        if cell.location == matrix_size - 2:
            return cell.distance + INSERTION
        if cell.location == matrix_size - row_size - 1:
            return cell.distance + DELETION
        if cell.location == matrix_size - row_size - 2:
            cost = 0 if source[row + 1] == target[col + 1] else SUBSTITUTION
            return cell.distance + cost

        if col == row_size - 1:
            cell_queue.put(Cell(cell.distance + DELETION, cell.location + row_size))
        elif row == max_row - 1:
            cell_queue.put(Cell(cell.distance + INSERTION, cell.location + row_size))
        else:
            cost = 0 if source[row + 1] == target[col + 1] else SUBSTITUTION
            cell_queue.put(Cell(cell.distance + INSERTION, cell.location + 1))
            cell_queue.put(Cell(cell.distance + DELETION, cell.location + row_size))
            cell_queue.put(Cell(cell.distance + cost, cell.location + row_size + 1))

if __name__=='__main__':
    check_triangle_validity()

    print(calculate_distance_greedy('aacc', 'aabbcc') == calculate_distance('aacc', 'aabbcc'))