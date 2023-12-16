MAX_CUBES: dict[str, int] = {"red": 12, "green": 13, "blue": 14}


def invalid_game(game_data: str) -> bool | None:
    for r in game_data.split("; "):
        for colour_data in r.split(", "):
            count, colour = colour_data.split()

            if int(count) > MAX_CUBES.get(colour):
                return True


with open("input.txt", "r") as f:
    game_sum = 0

    for game in f.readlines():
        game_id, game_data = game.split(": ")

        if not invalid_game(game_data):
            game_sum += int(game_id.split()[1])

print(game_sum)
