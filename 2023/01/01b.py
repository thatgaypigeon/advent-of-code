from re import findall as fa

WORDS: list[str] = [
    "N/A",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

sum = 0

with open("input.txt", "r") as f:
    for index, line in enumerate(f.readlines()):
        matches: list[str] = fa(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )

        d1: int | str = WORDS.index(matches[0]) if matches[0] in WORDS else matches[0]
        d2: int | str = (
            WORDS.index(matches[-1]) if matches[-1] in WORDS else matches[-1]
        )

        sum += int(str(d1) + str(d2))

print(sum)
