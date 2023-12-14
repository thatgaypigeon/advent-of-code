from itertools import groupby


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"

DM = DAMAGED
OP = OPERATIONAL
UN = UNKNOWN


def group(l: list, c: str) -> list[list]:
    """Split a list by grouping consecutive characters."""
    return [list(group) for key, group in groupby(l) if key != c]


def combinations(x: int, n: int) -> int:
    """Count the number of ways `n` consecutive chars can fit in a string of length `x`."""
    return x - n + 1 if x >= n else 0


def count_as(l: list, c: str, i: int) -> int:
    """Count the adjacent occurrences of char `c` in list `l` at index `i`."""
    count = 0
    l = l.copy()
    while l and l[i] == c:
        count += 1
        l.pop(i)
    return count


def count_start_as(l: list, c: str) -> int:
    """Count the adjacent occurrences of char `c` in list `l` at the start."""
    return count_as(l, c, 0)


def count_start_as_2(l: list, c1: str, c2: str) -> int | bool:
    """Check if list `l` starts with some number of char `c1` and then some number of char `c2`."""
    count_c1 = count_start_as(l, c1)
    count_c2 = count_start_as(l[count_c1:], c2) if count_c1 < len(l) else 0
    return (count_c1 + count_c2) if (count_c1 > 0 and count_c2 > 0) else False


def count_end_as(l: list, c: str) -> int:
    """Count the adjacent occurrences of char `c` in list `l` at the end."""
    return count_as(l, c, -1)


def count_end_as_2(l: list, c1: str, c2: str) -> int | bool:
    """Check if list `l` end with some number of char `c1` and then some number of char `c2`."""
    count_c1 = count_end_as(l, c1)
    count_c2 = count_end_as(l[:-count_c1], c2) if count_c1 < len(l) else 0
    return (count_c1 + count_c2) if (count_c1 > 0 and count_c2 > 0) else False


def count_all(l: list, c: str) -> int | bool:
    """Return :class:`int` if all items in list `l` are equal to char `c`, else :class:`False`."""
    return all(x == c for x in l) and len(l)


def remove_start_as(l: list, c: str) -> None:
    """Remove the adjacent occurrences of char `c` in list `l` at the start."""
    while l and l[0] == c:
        l.pop(0)


def remove_end_as(l: list, c: str) -> None:
    """Remove the adjacent occurrences of char `c` in list `l` at the end."""
    while l and l[-1] == c:
        l.pop(-1)


def remove_ends_as(l: list, c1: str, c2: str = None) -> None:
    """Remove the adjacent occurrences of char `c1` in list `l` at the start and char `c2` at the end."""
    c2 = c1 if c2 is None else c2
    remove_start_as(l, c1)
    remove_end_as(l, c2)


def remove_operational_ends(l: list) -> None:
    """Remove all OPERATIONAL characters (`.`) from both ends of list `l`."""
    remove_ends_as(l, OPERATIONAL)


def expand_damaged_ends(l: list, o: list) -> None:
    """Expand the ends of list `l` if the length of the DAMAGED characters (`#`) are shorted than entry in order `o`."""
    if l and l[0] == DAMAGED:
        l[: order[0]] = DAMAGED

    if l and l[-1] == DAMAGED:
        l[-order[-1]] = DAMAGED


def remove_damaged_ends(l: list, o: list) -> None:
    """Remove the ends of list `l` if the length of the DAMAGED characters (`#`) are equal to the entry in order `o`."""
    if l and count_start_as(springs, DAMAGED) == order[0]:
        del springs[: order[0]]
        del order[0]

    if l and count_end_as(springs, DAMAGED) == order[-1]:
        del springs[-order[-1] :]
        del order[-1]


def remove_unknown_ends(l: list, o: list) -> None:
    """If length of UNKNOWN (`?`) and DAMAGED (`#`) characters at ends of list `l` are larger than ends of order `o`, remove them."""
    if (c := count_start_as_2(springs, UNKNOWN, DAMAGED)) and c > o[0]:
        remove_start_as(l, UNKNOWN)

    if (c := count_end_as_2(springs, UNKNOWN, DAMAGED)) and c > o[-1]:
        remove_end_as(l, UNKNOWN)


def all_unknown(l: list, o: list) -> None:
    """Clear list `l` if all characters are UNKNOWN (`?`) and their length matches the minimum length of elements of order `o`."""
    if count_all(l, UNKNOWN) == sum(o) + len(o) - 1:
        l.clear()
        o.clear()


def no_damaged(l: list, o: list) -> bool:
    """Check if all characters in list `l` are UNKNOWN (`?`) or OPERATIONAL (`.`) and their groups are contained in order `o`."""
    return all(c in [UNKNOWN, OPERATIONAL] for c in l)


def count_arrangements(l: list, o: list) -> int:
    """Count the arrangements of elements in list `l` by elements in order `o` when split at OPERATIONAL characters (`.`)."""
    if not l:
        return 1

    arrs = 0
    for i, c in enumerate(group(l, OPERATIONAL)):
        arrs += combinations(len(c), o[i])
    return arrs


def possible_order(l: list, o: list) -> bool:
    """Return :class:`True` if elements of list `l` are all UNKNOWN (`?`) or OPERATIONAL (`.`) and can be ordered by elements in order `o`."""
    return no_damaged(l, o) and len(group(l, OPERATIONAL)) == len(o)


with open("input.txt", "r") as f:
    for line in f.readlines():
        springs = list(line.split(" ")[0])
        order = list(map(int, line.split(" ")[1].split(",")))

        # minimum arrangements
        arrangements = 0

        # reduce lists (uses no arrangements)
        while True:
            prev_springs = springs.copy()

            if springs:
                print(".", "".join(springs), order)

            remove_operational_ends(springs)

            if springs:
                print("#", "".join(springs), order)

            expand_damaged_ends(springs, order)
            remove_damaged_ends(springs, order)

            if springs:
                print("?", "".join(springs), order)

            remove_unknown_ends(springs, order)

            if springs:
                print("-", "".join(springs), order)

            # clear list if all elements are unknown and of minimum length needed for order
            all_unknown(springs, order)

            if springs:
                print("*", "".join(springs), order)

            if possible_order(springs, order):
                print("A")
                arrangements += count_arrangements(springs, order)
                break

            # break if list is empty (fully reduced; no arrangements; no ambiguity)
            if not springs:
                arrangements = 1
                break

            # break if list is unchanged (list is already reduced)
            if prev_springs == springs:
                arrangements = 1
                break

            print()

        print(f"\n== {str(arrangements)} ==".ljust(20, "="), "\n")

        # calculate arrangements
