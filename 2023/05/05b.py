locations: list[int] = []


def step(num_range: tuple[int, int], maps: list[str]):
    destn_ranges = []

    for map in maps:
        destn_start = int(map.split(" ")[0])
        source_start = int(map.split(" ")[1])
        range_length = int(map.split(" ")[2])

        if source_start <= num_range[1] and source_start + range_length >= num_range[0]:
            # Calculate the overlap
            overlap_start = max(source_start, num_range[0])
            overlap_end = min(source_start + range_length, num_range[1])

            destn_range_start = destn_start + (overlap_start - source_start)
            destn_range_end = destn_start + (overlap_end - source_start)

            destn_ranges.append((destn_range_start, destn_range_end))

    return destn_ranges


def parse_map(_map: str):
    return list(filter(None, _map.split("\n")[1:]))


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

    # Parse seeds as ranges
    seeds = []
    seed_ranges = list(map(int, data[0].split(" ")[1:]))
    for i in range(0, len(seed_ranges), 2):
        start = seed_ranges[i]
        length = seed_ranges[i + 1]
        seeds.append((start, start + length))

    maps = list(map(parse_map, data[1:]))

    for seed_range in seeds:
        value_ranges = [seed_range]

        for map in maps:
            new_value_ranges = []

            for value_range in value_ranges:
                new_value_ranges.extend(step(value_range, map))

            value_ranges = new_value_ranges

        locations.extend(value_ranges)

print(min(locations, key=lambda x: x[0])[0])
