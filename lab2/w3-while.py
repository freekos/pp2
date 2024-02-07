# While loop
i = 0
while i < 10:
    print(i)
    i += 1

# While loop with break and continue
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 3:
        continue
    if i == 7:
        break

# While loop with else
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 10")