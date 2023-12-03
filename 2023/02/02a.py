possible = set()
not_possible = set()

with open("input.txt", "r") as f:
    for line in f.readlines():
        game, rounds = line.strip().split(": ", 1)
        game_id = int(game.split(" ")[1])
        possible.add(game_id)

        for round_data in rounds.split("; "):
            round = dict((k, int(v)) for k, v in (reversed(s.split(" ")) for s in round_data.split(", ")))

            if not (
                (round.get("red") or 0) <= 12 and
                (round.get("green") or 0) <= 13 and
                (round.get("blue") or 0) <= 14
            ):
                not_possible.add(game_id)

print(sum(possible.difference(not_possible)))
