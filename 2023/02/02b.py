sum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        game: str
        rounds: str
        game, rounds = line.strip().split(": ", 1)

        red: int = 0
        green: int = 0
        blue: int = 0

        for round_data in rounds.split("; "):
            round = dict(
                (k, int(v))
                for k, v in (reversed(s.split(" ")) for s in round_data.split(", "))
            )

            red = (round.get("red") or 0) > red and round.get("red") or red
            blue = (round.get("blue") or 0) > blue and round.get("blue") or blue
            green = (round.get("green") or 0) > green and round.get("green") or green

        sum += red * green * blue

print(sum)
