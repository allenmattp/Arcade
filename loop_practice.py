print("\nProblem 1\n")

for i in range(10):
    print("*", end=" ")

print("\n\nProblem 2\n")

for i in range(10):
    print("*", end=" ")
print()
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
    print("*", end=" ")

print("\n\nProblem 3\n")

for i in range(10):
    print()
    for j in range(10):
        print("*", end=" ")

print("\n\nProblem 4\n")

for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()

print("\n\nProblem 5\n")

for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print()

print("\n\nProblem 6\n")

for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()

print("\n\nProblem 7\n")

for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print()

print("\n\nProblem 8\n")

for i in range(10):
    for j in range(i+1):
        print(j, end=" ")
    print()

print("\n\nProblem 9\n")

for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for j in range(10-i):
        print(j, end=" ")
    print()

print("\n\nProblem 10\n")

for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(" ", end="")
        print(i * j, end="  ")
    print()

print("\n\nProblem 11\n")

for i in range(1, 10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i-1):
        print(i - j - 1, end=" ")

    print()

for i in range(1, 10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

print("\n\nProblem 12\n")


for i in range(1, 10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
for i in range(8, 0, -1):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    print()

print("\n\nProblem 13\n")


for i in range(1, 10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
for i in range(8, 0, -1):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()