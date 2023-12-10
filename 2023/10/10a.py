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

        match char:
            case "." | " ":
                self.char = " " # "⬝"
                self.empty = True
            case "|":
                self.char = "│"
                self.path = "┃"
                self.north = True
                self.south = True
            case "-":
                self.char = "─"
                self.path = "━"
                self.east = True
                self.west = True
            case "F":
                self.char = "┌"
                self.path = "┏"
                self.south = True
                self.east = True
            case "7":
                self.char = "┐"
                self.path = "┓"
                self.south = True
                self.west = True
            case "L":
                self.char = "└"
                self.path = "┗"
                self.north = True
                self.east = True
            case "J":
                self.char = "┘"
                self.path = "┛"
                self.north = True
                self.west = True
            case "S":
                self.char = "★"
                self.path = "★"
                self.start = True
            case _:
                self.char = "🟥"

    def __str__(self) -> str:
        return self.visited and (self.path if self.path else self.char) or " "

def show_grid(grid: list[list[Pipe]]):
    for row in grid:
        print("".join(map(str, row)))

with open("input.txt", "r") as f:
    grid: list[list[Pipe]] = []
    start: Pipe

    for row_i, line in enumerate(f.readlines()):
        if not grid:
            grid.append([Pipe(" ", (char_i + 1, row_i)) for char_i in range(len(line))])

        row = [Pipe(" ", (0, row_i))]
        for char_i, char in enumerate(list(line.strip())):
            pipe = Pipe(char, (char_i + 1, row_i + 1))
            row.append(pipe)

            if pipe.start:
                start = pipe

        row.append(Pipe(char, (len(row) + 1, row_i)))

        grid.append(row)

    grid.append([Pipe(" ", (char_i, row_i)) for char_i in range(len(line))])

    start_coords = start.coords

    # identify starting directions
    if (pipe := grid[start.coords[1] - 1][start.coords[0]]) and pipe.south: # row above
        start.north = True
    if (pipe := grid[start.coords[1] + 1][start.coords[0]]) and pipe.north: # row below
        start.south = True
    if (pipe := grid[start.coords[1]][start.coords[0] + 1]) and pipe.west: # column right
        start.east = True
    if (pipe := grid[start.coords[1]][start.coords[0] - 1]) and pipe.east: # column left
        start.west = True

    pipe = start
    prev = start
    started = False
    counter = 0
    visited = []

    while not started or pipe.coords != start.coords:
        started = True
        counter += 1

        N = grid[pipe.coords[1] - 1][pipe.coords[0]]
        S = grid[pipe.coords[1] + 1][pipe.coords[0]]
        E = grid[pipe.coords[1]][pipe.coords[0] + 1]
        W = grid[pipe.coords[1]][pipe.coords[0] - 1]

        if pipe.north and N.south and N.coords != prev.coords: # row above
            prev = pipe
            pipe = N

        elif pipe.south and S.north and S.coords != prev.coords: # row below
            prev = pipe
            pipe = S

        elif pipe.east and E.west and E.coords != prev.coords: # column right
            prev = pipe
            pipe = E

        elif pipe.west and W.east and W.coords != prev.coords: # column left
            prev = pipe
            pipe = W

        else:
            break

        visited.append(pipe.coords)
        pipe.visited = True

    # show_grid(grid)

    print(int(counter / 2))
