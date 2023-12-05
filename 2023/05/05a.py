locations: list[int] = []


def step(num: int, maps: list[str]):
    for map in maps:
        destn = int(map.split(" ")[0])
        start = int(map.split(" ")[1])
        range = int(map.split(" ")[2])

        if start <= num <= start + range:
            diff = destn - start
            return num + diff

    return num


def parse_map(_map: str):
    return _map.split("\n")[1:]


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

    seeds = list(map(int, data[0].split(" ")[1:]))
    maps = list(map(parse_map, data[1:]))

    for seed in seeds:
        value = seed

        for map in maps:
            value = step(value, map)

        locations.append(value)

print(min(locations))
