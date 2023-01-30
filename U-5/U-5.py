print("a")
for i in range(1, 6):
    print("*" * i)

print("b")
MAX = 5

for i in range(1, MAX + 1):
    for j in range(MAX - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()




print("c")
print("")
MAX = 5

for i in range(1, MAX + 1):
    for j in range(i):
        print(" ", end="")
    for k in range((2 * MAX - 1) - 2*i+2):
        print("*", end="")
    print()


print("")
print("")
print("")
print("d")

MAX = 5

for i in range(1, MAX+1):
    for j in range(MAX-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print(j, end="")
    print()


print("")
print("")
print("")
print("e")
MAX = 5

for i in range(1, MAX+1):
    for j in range(MAX-i):
        print(" ", end="")
    for j in range(MAX, MAX-i, -1):
        print("*", end="")
    for j in range(MAX-i+2, MAX+1):
        print("*", end="")
    print()

for i in range(1, MAX+1):
    for j in range(i):
        print(" ", end="")
    for j in range(MAX, i, -1):
        print("*", end="")
    for j in range(i+2, MAX+1):
        print("*", end="")
    print()
