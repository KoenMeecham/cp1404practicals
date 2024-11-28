for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c

stars = int(input("Choose the number of stars: "))
for i in range(stars):
    print("*", end=' ')
print()

# d
stars = int(input("Choose the number of stars: "))
for i in range(1, stars + 1):
    print("*" * i)
print()
