# Create dictionary by literal
d = {1: 2, 3: 4}
print(d)

# Create dictionary by constructor
d = dict(a = 2, b = 4)
print(d)

# Dictionary type
d = {1: 2, 3: 4}
print(type(d))

# Access by key
d = {1: 2, 3: 4}
print(d[1])

# Access by get method
d = {1: 2, 3: 4}
print(d.get(3))

# Get all keys
d = {1: 2, 3: 4}
print(d.keys())

# Get all values
d = {1: 2, 3: 4}
print(d.values())

# Get all items
d = {1: 2, 3: 4}
print(d.items())

# Check the contains
d = {1: 2, 3: 4}
print(1 in d)

# Change item by key
d = {1: 2, 3: 4}
d[1] = 3
print(d)

# Change item by update method
d = {1: 2, 3: 4}
d.update({1: 3})
print(d)

# Delete item by key
d = {1: 2, 3: 4}
del d[1]
print(d)

# Delete item by pop method
d = {1: 2, 3: 4}
d.pop(1)
print(d)

# Delete item by clear method
d = {1: 2, 3: 4}
d.clear()
print(d)

# Copy by copy method
d = {1: 2, 3: 4}
d2 = d.copy()
print(d2)

# Copy by new dictionary
d = {1: 2, 3: 4}
d2 = dict(d)
print(d2)

# Nested data structure
d = {1: 2, 3: {4: 5, 6: 7}}
print(d)
