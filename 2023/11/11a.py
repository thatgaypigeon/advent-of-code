from math import comb as nCr
from math import sqrt

GALAXY = "#"
EMPTY = "."


class Cell:
    def __init__(self, char: str, coords: tuple[int, int]):
        self.galaxy: bool = char == GALAXY
        self.char: str = char

        self.x: int = coords[0]
        self.y: int = coords[1]
        self.coords: tuple[int, int] = coords

    def __str__(self) -> str:
        return self.char


def is_empty(cell: str) -> bool:
    return cell == EMPTY

def calculate_distance(pair: tuple[tuple[int, int]]) -> int:
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

    expanded_grid: list = []
    galaxies = []

    for ri, row in enumerate(grid):
        if all(list(map(is_empty, row))):
            expanded_grid.append(row)
            expanded_grid.append(row.copy())
        else:
            expanded_grid.append(row)

    empty_cols = 0
    columns: list[list[str]] = [list(col) for col in zip(*grid)]
    for ci, col in enumerate(columns):
        if all(list(map(is_empty, col))):
            for row in expanded_grid:
                row.insert(ci + empty_cols, ".")
            empty_cols += 1

    smol_grid, grid = grid, expanded_grid

    # transform grid
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            cell = Cell(cell, (ci, ri))
            if cell.galaxy:
                galaxies.append(cell.coords)

    # show_grid(grid)

    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            pair = (galaxies[i], galaxies[j])
            distance = calculate_distance(pair)
            distances.append(distance)

    print(len(galaxies), nCr(len(galaxies), 2))

    print(sum(distances))
