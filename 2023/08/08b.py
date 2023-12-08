from math import gcd


def lmap(func, _list: list) -> list:
    return list(map(func, _list))


def dir_to_int(direction: str):
    states = ["L", "R"]
    return states.index(direction)


def is_end(node: str) -> bool:
    return node != "" and node[-1] == "Z"


with open("input.txt", "r") as f:
    lines: list[str] = lmap(str.strip, f.readlines())

    directions = lmap(dir_to_int, list(lines[0].strip()))

    nodes = {}

    for line in lines[2:]:
        line = line.strip()

        [node, connections] = line.split(" = ")
        connections = tuple(connections.strip("(").strip(")").split(", "))
        nodes.setdefault(node, connections)

    counts = []

    for node in nodes:
        if node[2] == "A":
            start = node
            end = "ZZZ"

            cur_node = start
            index = 0
            count = 0

            while cur_node[2] != "Z":
                cur_node = nodes[cur_node][directions[index % len(directions)]]
                index += 1
                count += 1

            counts.append(count)

    lcm = 1
    for i in counts:
        lcm *= i // gcd(lcm, i)

    print(lcm)
