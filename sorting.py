import random

list = []
for i in range(10000):
    list.append(random.randrange(1, 11))

print(list)

def selection_sort(my_list):
    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan list from left to right
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # Check to see if this position is the smallest
            if my_list[scan_pos] < my_list[min_pos]:
                # If it is, update the min_pos variable
                min_pos = scan_pos

        # Swap the two values in the list
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

# selection_sort(list)

def insertion_sort(my_list):

    # Start at the second element
    for key_pos in range(1, len(my_list)):

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to left
        scan_pos = key_pos - 1

        # Loop each element, moving them until...
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything has been moved, insert key into correct location
        my_list[scan_pos + 1] = key_value

insertion_sort(list)

print(list)

















"""print(list)
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0

for i in range(len(list)):
    if list[i] == 1:
        one += 1
    elif list[i] == 2:
        two += 1
    elif list[i] == 3:
        three += 1
    elif list[i] == 4:
        four += 1
    elif list[i] == 5:
        five += 1
    elif list[i] == 6:
        six += 1
    elif list[i] == 7:
        seven += 1
    elif list[i] == 8:
        eight += 1
    elif list[i] == 9:
        nine += 1
    elif list[i] == 10:
        ten += 1

print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)"""