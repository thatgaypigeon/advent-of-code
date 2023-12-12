from math import comb as nCr
from math import sqrt

GALAXY = "#"
EMPTY = "."

RATE_OF_EXPANSION = 1_000_000


class Cell:
    def __init__(self, char: str, coords: tuple[int, int]):
        self.galaxy: bool = char == GALAXY
        self.char: str = char

        self.coords: tuple[int, int] = coords

    def __str__(self) -> str:
        return self.char


def is_empty(cell: str) -> bool:
    return cell == EMPTY


def calculate_distance(pair: tuple[tuple[int, int], tuple[int, int]]) -> int:
    """Calculate distance with the Manhattan distance formula."""
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return abs(x2 - x1) + abs(y2 - y1)


def show_grid(grid: list[list[str]]) -> None:
    print("\n".join(["".join(row) for row in grid]))


grid: list = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

    empty_rows: list = []
    empty_cols: list = []
    galaxies: list = []

    for ri, row in enumerate(grid):
        if all(list(map(is_empty, row))):
            empty_rows.append(ri)

    columns: list[list[str]] = [list(col) for col in zip(*grid)]
    for ci, col in enumerate(columns):
        if all(list(map(is_empty, col))):
            empty_cols.append(ci)

    # transform grid
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            cell = Cell(cell, (ri, ci))
            if cell.galaxy:
                galaxies.append(cell.coords)

    # show_grid(grid)

    distances = {}
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            pair = (galaxies[i], galaxies[j])

            a_row = pair[0][0]
            a_col = pair[0][1]

            b_row = pair[1][0]
            b_col = pair[1][1]

            min_col = min(a_col, b_col)
            max_col = max(a_col, b_col)

            min_row = min(a_row, b_row)
            max_row = max(a_row, b_row)

            cols = [i for i in empty_cols if min_col < i < max_col]
            rows = [i for i in empty_rows if min_row < i < max_row]

            d = calculate_distance(pair)
            distance = d + ((RATE_OF_EXPANSION - 1) * (len(rows) + len(cols)))
            distances[pair] = distance

    print(sum(distances.values()))
