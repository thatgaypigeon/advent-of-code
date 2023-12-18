sum = 0

with open("input.txt", "r") as f:
    grid: list = []

    for line in f.readlines():
        grid.append(list("." + line.strip() + "."))

    for row_index, row in enumerate(grid):
        cur_num = ""
        num_start = None
        num_end = None

        for index, char in enumerate(row):
            if char.isdigit():
                num_start = index if num_start is None else num_start
                cur_num += char

            elif num_start is not None:
                num_end = (index - 1) if num_end is None else num_end

                is_lonely = True

                for row_to_check in range(row_index - 1, row_index + 2):
                    if 0 <= row_to_check < len(grid):
                        for char_to_check in range(num_start - 1, num_end + 2):
                            if 0 <= char_to_check < len(grid[row_to_check]):
                                if (
                                    check_char := grid[row_to_check][char_to_check]
                                ) != "." and (not check_char.isdigit()):
                                    is_lonely = False
                                    break

                if not is_lonely:
                    sum += int(cur_num)

                cur_num = ""
                num_start = None
                num_end = None

print(sum)
