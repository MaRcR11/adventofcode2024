def parse_grid(lines):
    return {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}


def can_place_obstruction(pos, grid, start_pos):
    return pos != start_pos and grid.get(pos, ".") not in ["#", "^"]


def simulate_guard_path(grid, start_pos):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pos = start_pos
    dir_idx = 0
    path = []

    while pos in grid and grid[pos] != "#":
        path.append((pos, dir_idx))
        new_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])
        if grid.get(new_pos) in ["#", "O"]:
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = new_pos
        if (pos, dir_idx) in path:
            break
    return path


def is_loop_with_obstruction(grid, start_pos, obstruction_pos):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pos = start_pos
    dir_idx = 0
    visited_states = set()

    while True:
        state = (pos, dir_idx)
        if state in visited_states:
            return True
        visited_states.add(state)

        new_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])

        if new_pos == obstruction_pos or grid.get(new_pos) in ["#", "O"]:
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = new_pos

        if pos not in grid:
            return False


def find_valid_obstruction_positions(grid):
    start_pos = next((p for p, c in grid.items() if c == "^"), None)
    if not start_pos:
        return 0

    guard_path = set(pos for pos, _ in simulate_guard_path(grid, start_pos))

    valid_positions = 0
    for pos in guard_path:
        if can_place_obstruction(pos, grid, start_pos):
            grid[pos] = "O"
            if is_loop_with_obstruction(grid, start_pos, pos):
                valid_positions += 1
            grid[pos] = "."

    return valid_positions


with open("input.txt") as f:
    grid = parse_grid([line.strip() for line in f])

result = find_valid_obstruction_positions(grid)
print(result)
