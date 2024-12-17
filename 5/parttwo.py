from collections import defaultdict, deque


def load_rules(rules_file):
    with open(rules_file) as f:
        rules = {int(y): set() for x, y in (line.strip().split("|") for line in f)}
        for x, y in (line.strip().split("|") for line in open(rules_file)):
            rules[int(y)].add(int(x))
    return rules


def load_updates(input_file):
    with open(input_file) as f:
        return [list(map(int, line.strip().split(","))) for line in f]


def is_valid_update(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    return all(
        position[x] < position[y]
        for y, x_set in rules.items()
        if y in position
        for x in x_set
        if x in position
    )


def topo_sort(update, rules):
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    for y in update:
        for x in rules.get(y, []):
            if x in update:
                graph[x].add(y)
                in_degree[y] += 1

    queue = deque(page for page in update if in_degree[page] == 0)
    reordered = []

    while queue:
        current = queue.popleft()
        reordered.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return reordered


def calculate_reordered_middle_sum(rules_file, input_file):
    rules = load_rules(rules_file)
    updates = load_updates(input_file)

    invalid_updates = [
        update for update in updates if not is_valid_update(update, rules)
    ]
    reordered_updates = [topo_sort(update, rules) for update in invalid_updates]

    return sum(update[len(update) // 2] for update in reordered_updates)


rules_file = "rules.txt"
input_file = "input.txt"

print(calculate_reordered_middle_sum(rules_file, input_file))
