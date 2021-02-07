count = 10
for i in range(10):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

rows = int(input("Enter desired size: "))
for i in range(rows):
    for j in range(rows * 2):
        if not i or i == rows-1:
            print("o", end="")
    if i > 0 and i != rows - 1:
        print("o", end="")
        for space in range(rows * 2 - 2):
            print(" ", end="")
        print("o")
    else:
        print()

rows = int(input("Enter value for n: "))
for i in range(rows):
    print()
    for j in range(rows - i):
        print(j * 2 + 1 + i * 2, end=" ")
    for j in range(i):
        print("  ", end="  ")
    for j in range(rows - i, 0, -1):
        print(j * 2 - 1 + i * 2, end=" ")

for i in range(rows, 0, -1):
    print()
    for j in range(rows - i + 1):
        print(j * 2 + i * 2 - 1, end=" ")
    for j in range(i-1):
        print("  ", end="  ")
    for j in range(rows - i + 1, 0, -1):
        print(j * 2 + i * 2 - 3, end=" ")

