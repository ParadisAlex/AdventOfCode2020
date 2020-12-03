import os

map = open(os.path.join(os.getcwd(), "day3_input.txt"), "r").read().splitlines()


def get_tree_count(x_angle, y_angle):
    x = 0
    y = 0
    trees = 0
    while y < len(map):
        line = map[y]
        if x >= len(line):
            x = 0 + (x - len(line))
        if line[x] == '#':
            trees += 1
        x += x_angle
        y += y_angle
    return trees

def part2():
    a = get_tree_count(1, 1)
    b = get_tree_count(3, 1)
    c = get_tree_count(5, 1)
    d = get_tree_count(7, 1)
    e = get_tree_count(1, 2)
    return a*b*c*d*e

print("First part answer: {}".format(get_tree_count(3, 1)))
print("Part two answer: {}".format(part2()))
