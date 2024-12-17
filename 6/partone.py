def parse_grid(lines):
    return {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}


def traverse_grid(grid):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pos = next((p for p, c in grid.items() if c == "^"), None)
    if not pos:
        return 0

    visited, dir_idx = set(), 0
    while pos in grid:
        visited.add(pos)
        new_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])
        if grid.get(new_pos) == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = new_pos
    return len(visited)


with open("input.txt") as f:
    grid = parse_grid([line.strip() for line in f])

print(traverse_grid(grid))
