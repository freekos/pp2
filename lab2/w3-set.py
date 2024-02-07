# Literal construction
s = {1, 2, 3, 3}
print(s)

# Type printing
s = {1, 2, 3}
print(type(s))

# Access to set items
s = {1, 2, 3}
for i in s:
    print(i)
print(1 in s)

# Add item to set
s = {1, 2, 3}
s.add(4)
print(s)

# Add iterable collection to set
s = {1, 2, 3}
s2 = {7, 8}
s.update([4, 5, 6], s2)
print(s)

# Remove item from set
s = {1, 2, 3}
s.remove(1)
print(s)

# Remove many items from set
s = {1, 2, 3}
s.difference_update({1, 2})
print(s)

# Pop random item from set
s = {1, 2, 3}
s.pop()
print(s)

# Delete set
s = {1, 2, 3}
s.clear()
print(s)

# Join set
s = {1, 2, 3}
s = s.union({5, 4})
print(s)