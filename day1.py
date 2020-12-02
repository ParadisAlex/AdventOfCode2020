import os

day1_arr = open(os.path.join(os.getcwd(), "day_1_input.txt"), "r").read().split('\n')
print("List has {} elements".format(len(day1_arr)))

def day1_part1():
    for item in day1_arr:
        i = 0
        while i < len(day1_arr):
            sum = int(item) + int(day1_arr[i])
            if sum == 2020:
                product = int(item) * int(day1_arr[i])
                print(
                    "The two elements that have a sum of 2020 in this array are {} and {} with their product being {}".format(
                        item,
                        day1_arr[i],
                        product))
                return product
            i = i + 1

def day1_part2():
    for item in day1_arr:
        indexA = 0
        while indexA < len(day1_arr):
            indexB = 0
            while indexB < len(day1_arr):
                sum = int(item) + int(day1_arr[indexA]) + int(day1_arr[indexB])
                if sum == 2020:
                    product = int(item) * int(day1_arr[indexA]) * int(day1_arr[indexB])
                    print("The three elements that have a sum of 2020 in this array are {}, {} and {} with a product of {}".format(
                        item,
                        day1_arr[indexA],
                        day1_arr[indexB],
                        product
                    ))
                    return product
                indexB = indexB + 1
            indexA = indexA + 1

day1_part1 = day1_part1()
day1_part2 = day1_part2()

