def count_word_occurrences(grid, word):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def is_valid(x, y, dx, dy):
        return all(
            0 <= x + i * dx < len(grid)
            and 0 <= y + i * dy < len(grid[0])
            and grid[x + i * dx][y + i * dy] == word[i]
            for i in range(len(word))
        )

    return sum(
        is_valid(x, y, dx, dy)
        for x in range(len(grid))
        for y in range(len(grid[0]))
        for dx, dy in directions
    )


with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]
    print(grid)

word = "XMAS"

print(count_word_occurrences(grid, word))
