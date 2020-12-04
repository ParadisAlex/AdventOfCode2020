import os
from objects.credential import Credential


with open(os.path.join(os.getcwd(), "day4_input.txt"), "r") as f:
    raw = f.read().splitlines()

batch = []
# convert each input group into one single string to pass to Credential class
line = ""
i = 0
while i < len(raw):
    if raw[i] != '':
        line = raw[i] + ' ' + line
        if i == len(raw) - 1:
            cred = Credential(line)
            batch.append(cred)
    else:
        cred = Credential(line)
        batch.append(cred)
        line = "" # reset if line empty, indicates new entry
    i += 1

print("{} total entries".format(len(batch)))

part1_valid = 0
for item in batch:
    if item.is_valid():
        part1_valid += 1
print("PART1: There are {} valid credentials in this list.".format(part1_valid))

part2_valid = 0
for item in batch:
    if item.is_extra_valid():
        part2_valid += 1

print("PART2: There are {} valid credentials in this list.".format(part2_valid))