def load_rules(rules_file):
    with open(rules_file) as f:
        rules = {int(y): set() for x, y in (line.strip().split('|') for line in f)}
        for x, y in (line.strip().split('|') for line in open(rules_file)):
            rules[int(y)].add(int(x))
    return rules

def load_updates(input_file):
    with open(input_file) as f:
        return [list(map(int, line.strip().split(','))) for line in f]

def is_valid_update(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    return all(position[x] < position[y] for y, x_set in rules.items() if y in position for x in x_set if x in position)

def calculate_middle_sum(rules_file, input_file):
    rules = load_rules(rules_file)
    updates = load_updates(input_file)
    return sum(update[len(update) // 2] for update in updates if is_valid_update(update, rules))

rules_file = "rules.txt"
input_file = "input.txt"

print(calculate_middle_sum(rules_file, input_file))
