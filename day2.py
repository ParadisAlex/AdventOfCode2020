import os

passwords = open(os.path.join(os.getcwd(), "day2_input.txt"), "r").read().splitlines()

def part1():
    valid_passwords = 0
    for password in passwords:
        policy_letter = password.split(':')[0].split(' ')[1]
        min_max = password.split(':')[0].split(' ')[0]
        min = int(min_max.split('-')[0])
        max = int(min_max.split('-')[1])
        pwd = password.split(':')[1].strip()
        if min <= pwd.count(policy_letter) <= max:
            valid_passwords = valid_passwords + 1
    return valid_passwords

def part2():
    valid_passwords = 0
    for password in passwords:
        policy_letter = password.split(':')[0].split(' ')[1]
        pwd = password.split(':')[1].strip()
        indexes = password.split(':')[0].split(' ')[0]
        index1 = pwd[int(indexes.split('-')[0]) - 1]
        index2 = pwd[int(indexes.split('-')[1]) - 1]
        if (index1 == policy_letter or index2 == policy_letter) and index1 != index2:
            valid_passwords = valid_passwords + 1
    return valid_passwords

print("Part one answer: {}".format(part1()))
print("Part two answer: {}".format(part2()))