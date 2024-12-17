def count_x_word_patterns(grid, word):
    def is_x_pattern(x, y):
        if 1 <= x < len(grid) - 1 and 1 <= y < len(grid[0]) - 1:
            corners = [grid[x - 1][y - 1], grid[x + 1][y + 1], grid[x - 1][y + 1], grid[x + 1][y - 1]]
            return (
                grid[x][y] == word[1] and 
                set(corners[:2]) == {word[0], word[2]} and  
                set(corners[2:]) == {word[0], word[2]}     
            )
        return False

    return sum(
        is_x_pattern(x, y)
        for x in range(1, len(grid) - 1)
        for y in range(1, len(grid[0]) - 1)
    )

with open("input.txt", 'r') as file:
    grid = [list(line.strip()) for line in file]

word = "MAS"

print(count_x_word_patterns(grid, word))
