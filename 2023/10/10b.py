import sys

sys.setrecursionlimit(1000000000)


class Pipe:
    def __init__(self, char: str, coords: tuple[int, int]) -> None:
        self.north: bool = False
        self.south: bool = False
        self.east: bool = False
        self.west: bool = False

        self.char: str
        self.orig_char: str = char

        self.empty: bool = False
        self.start: bool = False

        self.coords: tuple[int, int] = coords
        self.x: int = coords[0]
        self.y: int = coords[1]

        self.visited = False
        self.path = False

        self.inside_h: bool = False
        self.inside_v: bool = False

        match char:
            case "." | " ":
                self.char = " "  # "⬝"
                self.empty = True
            case "|" | "│":
                self.char = "│"
                self.path = "┃"
                self.north = True
                self.south = True
            case "-" | "─":
                self.char = "─"
                self.path = "━"
                self.east = True
                self.west = True
            case "F" | "┌":
                self.char = "┌"
                self.path = "┏"
                self.south = True
                self.east = True
            case "7" | "┐":
                self.char = "┐"
                self.path = "┓"
                self.south = True
                self.west = True
            case "L" | "└":
                self.char = "└"
                self.path = "┗"
                self.north = True
                self.east = True
            case "J" | "┘":
                self.char = "┘"
                self.path = "┛"
                self.north = True
                self.west = True
            case "S" | "★":
                self.char = "★"
                self.path = "★"
                self.start = True
            case _:
                self.char = "🟥"

    def __str__(self) -> str:
        if not self.visited and self.inside_h and self.inside_v:
            return "#"
        elif self.empty:
            return " "
        else:
            return self.visited and (self.path if self.path else self.char) or " "

    def __repr__(self) -> str:
        return f"{self.coords} {self.visited and (self.path if self.path else self.char) or self.char}"


def show_grid(grid: list[list[Pipe]]) -> None:
    for row in grid:
        print("".join(map(str, row)))


def thiccen(grid: list[list[Pipe]]) -> list[list[Pipe]]:
    grid_size = len(grid)
    row_size = len(grid[0])

    thicc_grid: list[list[Pipe]] = [
        [0 for pipe in range(row_size * 3)] for row in range(grid_size * 3)
    ]

    thicc_pipes: dict[str, list[list[str]]] = {
        " ": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        "│": [[" ", "│", " "], [" ", "│", " "], [" ", "│", " "]],
        "─": [[" ", " ", " "], ["─", "─", "─"], [" ", " ", " "]],
        "┌": [[" ", " ", " "], [" ", "┌", "─"], [" ", "│", " "]],
        "┐": [[" ", " ", " "], ["─", "┐", " "], [" ", "│", " "]],
        "└": [[" ", "│", " "], [" ", "└", "─"], [" ", " ", " "]],
        "┘": [[" ", "│", " "], ["─", "┘", " "], [" ", " ", " "]],
    }

    thicc_start: list[list[str]] = [[" ", " ", " "], [" ", "★", " "], [" ", " ", " "]]

    for row in grid:
        for pipe in row:
            # input(repr(pipe))
            if pipe.start:
                if pipe.north:
                    thicc_start[0][1] = "│"
                    if pipe.east:
                        thicc_start[1][1] = "┘"
                        thicc_start[1][2] = "─"
                    elif pipe.west:
                        thicc_start[1][1] = "└"
                        thicc_start[1][0] = "─"
                elif pipe.south:
                    thicc_start[2][1] = "│"
                    if pipe.east:
                        thicc_start[1][1] = "┌"
                        thicc_start[1][2] = "─"
                    elif pipe.west:
                        thicc_start[1][1] = "┐"
                        thicc_start[1][0] = "─"

                sub_grid = thicc_start
            else:
                sub_grid = thicc_pipes[pipe.char]

            for sr_i, sub_row in enumerate(sub_grid):
                # print("".join(sub_row))
                for sp_i, sub_char in enumerate(sub_row):
                    # print(((pipe.coords[0] * 3) + sp_i, , sub_pipe)
                    sub_pipe_coords = (
                        (pipe.coords[0] * 3) + sp_i,
                        (pipe.coords[1] * 3) + sr_i,
                    )
                    sub_pipe = Pipe(sub_char, sub_pipe_coords)

                    if pipe.visited:
                        sub_pipe.visited = True

                    thicc_grid[sub_pipe_coords[1]][sub_pipe_coords[0]] = sub_pipe
                    # print(sub_pipe)
                    # print(Pipe(sub_pipe, sub_pipe_coords))
                    # input()

    return thicc_grid


with open("input.txt", "r") as f:
    grid: list[list[Pipe]] = []
    start: Pipe

    for row_i, line in enumerate(f.readlines()):
        row = []
        for char_i, char in enumerate(list(line.strip())):
            pipe = Pipe(char, (char_i, row_i))
            row.append(pipe)

            if pipe.start:
                start = pipe

        grid.append(row)

    start_coords = start.coords

    # identify starting directions
    if (pipe := grid[start.coords[1] - 1][start.coords[0]]) and pipe.south:  # above
        start.north = True
    if (pipe := grid[start.coords[1] + 1][start.coords[0]]) and pipe.north:  # below
        start.south = True
    if (pipe := grid[start.coords[1]][start.coords[0] + 1]) and pipe.west:  # right
        start.east = True
    if (pipe := grid[start.coords[1]][start.coords[0] - 1]) and pipe.east:  # left
        start.west = True

    pipe = start
    prev = start
    started = False
    counter = 0
    visited = []

    while not started or pipe.coords != start.coords:
        started = True
        counter += 1

        try:
            N = grid[pipe.coords[1] - 1][pipe.coords[0]]
        except IndexError:
            N = Pipe(" ", (0, 0))

        try:
            S = grid[pipe.coords[1] + 1][pipe.coords[0]]
        except IndexError:
            S = Pipe(" ", (0, 0))

        try:
            E = grid[pipe.coords[1]][pipe.coords[0] + 1]
        except IndexError:
            E = Pipe(" ", (0, 0))

        try:
            W = grid[pipe.coords[1]][pipe.coords[0] - 1]
        except IndexError:
            W = Pipe(" ", (0, 0))

        if pipe.north and N.south and N.coords != prev.coords:  # row above
            prev = pipe
            pipe = N

        elif pipe.south and S.north and S.coords != prev.coords:  # row below
            prev = pipe
            pipe = S

        elif pipe.east and E.west and E.coords != prev.coords:  # column right
            prev = pipe
            pipe = E

        elif pipe.west and W.east and W.coords != prev.coords:  # column left
            prev = pipe
            pipe = W

        else:
            break

        visited.append(pipe.coords)
        pipe.visited = True

    for row in grid:
        for pipe in row:
            if not pipe.visited:
                pipe.empty = True

    grid = thiccen(grid)

    # get inside area (h)
    for ri, row in enumerate(grid):
        c = 0
        n = 0
        s = 0
        for pi, pipe in enumerate(row):
            prev: Pipe
            if pipe.visited and pipe.north:
                n += 1
            if pipe.visited and pipe.south:
                s += 1
            if not pipe.visited and n % 2 == 1 and s % 2 == 1:
                pipe.inside_h = True

    # get inside area (v)
    columns = [list(col) for col in zip(*grid)]
    for index, column in enumerate(columns):
        e = 0
        w = 0
        for pipe in column:
            prev: Pipe
            if pipe.visited and pipe.east:
                e += 1
            if pipe.visited and pipe.west:
                w += 1
            if not pipe.visited and e % 2 == 1 and w % 2 == 1:
                pipe.inside_v = True

    inside_count = 0

    # transform back to original grid
    smol_grid = []
    for row in grid[1::3]:
        smol_row = []

        for pipe in row[1::3]:
            smol_row.append(pipe)

            if pipe.inside_v and pipe.inside_h:
                inside_count += 1

        smol_grid.append(smol_row)

    # show_grid(smol_grid)

    print(inside_count)
