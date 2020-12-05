import os


def get_id(ticket):
    # first convert row and column to binary
    row = ticket[:7].replace("F", "0").replace("B", "1")
    col = ticket[7:].replace("L", "0").replace("R", "1")
    # convert to base10 integers
    row = int(row, 2)
    col = int(col, 2)

    return row*8 + col


with open(os.path.join(os.getcwd(), "day5_input.txt"), "r") as f:
    raw = f.read().splitlines()

seats = []
for item in raw:
    seats.append(get_id(item))


print("Max value for ticket id is: {}".format(max(seats)))

# Part2

for seat in seats:
    if seat + 1 not in seats:
        print(seat+1)