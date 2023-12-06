def parse_input(data: list[str]) -> list[tuple[int, int]]:
    pairs = []

    times = []
    distances = []

    time = data[0]
    distance = data[1]

    time = time.split(":")[1].split(" ")
    for a in time:
        if a:
            times.append(int(a))

    distance = distance.split(":")[1].split(" ")
    for a in distance:
        if a:
            distances.append(int(a))

    for index, time in enumerate(times):
        pairs.append((time, distances[index]))

    return pairs


num_ways = []

with open("input.txt", "r") as f:
    races = parse_input(f.readlines())

    print(races)

    for race in races:
        strategies = 0

        time = race[0]
        distance = race[1]

        for i in range(time):
            if (time - i) * i > distance:
                strategies += 1

        num_ways.append(strategies)

product = 1
for i in num_ways:
    product = product * i

print(product)
