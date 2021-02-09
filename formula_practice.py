import math
import random

def main():
    def min3(x, y, z):
        if x <= y and x <= z:
            return x
        elif y <= x and y <= z:
            return y
        else:
            return z

    print(min3(4, 7, 5))
    print(min3(4, 5, 5))
    print(min3(4, 4, 4))
    print(min3(-2, -6, -100))
    print(min3("Z", "B", "A"))

    def box(height, width):
        for h in range(height):
            for w in range(width):
                print("*", end="")
            print()

    box(7, 5)  # Print a box 7 high, 5 across
    print()  # Blank line
    box(3, 2)  # Print a box 3 high, 2 across
    print()  # Blank line
    box(3, 10)  # Print a box 3 high, 10 across

    def find(my_list, key):
        for i in range(len(my_list)):
            if my_list[i] == key:
                print("Found", my_list[i], "at position", i)

    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

    find(my_list, 12)
    find(my_list, 91)
    find(my_list, 80)

    def create_list(size):
        my_list = []
        for i in range(size):
            my_list.append(random.randrange(1,11))
        return my_list

    my_list = create_list(5)
    print(my_list)

    def count_list(list, number):
        count = 0
        for i in range(len(list)):
            if list[i] == number:
                count += 1
        return count

    count = count_list([1, 2, 3, 3, 3, 4, 2, 1], 3)
    print(count)

    def average_list(list):
        average = 0
        for i in range(len(list)):
            average += list[i]
        return (average / len(list))

    avg = average_list([1, 2, 3])
    print(avg)

    lab_list = create_list(100000000)
    for i in range(1,11):
        print("Found", i, count_list(lab_list, i), "times")
    print(average_list(lab_list))

if __name__ == "__main__":
    main()