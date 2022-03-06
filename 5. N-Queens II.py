from typing import List


state = List[int]


def queens(size: int) -> int:
    return len(queens_recursive([], [], size))


def queens_recursive(state: state,
                     solutions: List[state],
                     size: int) -> List[state]:
    if len(state) == size:
        solutions.append(state[:])
        return solutions

    for row in range(size):
        if queen_check(state, row):
            state.append(row)
            queens_recursive(state, solutions, size)
            state.pop()

    return solutions


def queen_check(state: state, new_row: int) -> bool:
    new_col = len(state)
    for col, row in enumerate(state):
        if row == new_row or abs(row - new_row) == abs(col - new_col):
            return False
    return True


print(queens(3))
