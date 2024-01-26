# Create
print("--Create--")
a = (1, 2, 3)
print(a)

# Try to modify
# print("--Modify--")
# a = (1, 2, 3)
# a[0] = 2
# print(a)

# Length
print("--Length--")
a = (1, 2, 3)
print(len(a))

# Single item tuple
print("--Single--item--tuple--")
a = (1,)
b = (1)
print(a)
print(type(a))
print(b)
print(type(b))

# Access tuples
print("--Access--tuples--")
a = (1, 2, 3)
print(a)
print(a[0])
print(a[:1])
print(a[1:])

# Try to modify second one
print("--Modify--second--one--")
a = (1, 2, 3)
b = list(a)
b.append(4)
a = tuple(b)
print(a)

#Unpack
print("--Unpack--")
a, b, c = (1, 2, 3)
print(a, b, c)
a, *b, c = (1, 2, 3, 4, 5, 6)
print(a, b, c)

# Loop
print("--Loop--")
a = (1, 2, 3)
for item in a:
    print(item)
for i in range(len(a)):
    print(a[i])

# Join
print("--Join--")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
print(tuple1*3)