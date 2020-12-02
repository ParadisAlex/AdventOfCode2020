import os

arr = open(os.path.join(os.getcwd(), "day_1_input.txt"), "r").read().split('\n')
print("List has {} elements".format(len(arr)))

def day1_part1():
    for item in arr:
        i = 0
        while i < len(arr):
            sum = int(item) + int(arr[i])
            if sum == 2020:
                product = int(item) * int(arr[i])
                print(
                    "The two elements that have a sum of 2020 in this array are {} and {} with their product being {}".format(
                        item,
                        arr[i],
                        product))
                return product
            i = i + 1

def day1_part2():
    for item in arr:
        indexA = 0
        while indexA < len(arr):
            indexB = 0
            while indexB < len(arr):
                sum = int(item) + int(arr[indexA]) + int(arr[indexB])
                if sum == 2020:
                    product = int(item) * int(arr[indexA]) * int(arr[indexB])
                    print("The three elements that have a sum of 2020 in this array are {}, {} and {} with a product of {}".format(
                        item,
                        arr[indexA],
                        arr[indexB],
                        product
                    ))
                    return product
                indexB = indexB + 1
            indexA = indexA + 1

day1_part1 = day1_part1()
day1_part2 = day1_part2()

