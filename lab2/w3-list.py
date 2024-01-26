# List
print("--List--")
a = [1, "Hello", True]
print(a)
print(type(a))
print(a[0])
print(type(a[0]))
print(1 in a)
print(True in a)
print(a[:5])
print(a[5:])

# List mutation
print("--List--mutation--")
a = [1, 2, 3]
print(a)
a.append(4)
print(a)
a.insert(0, 0)
print(a)
a[0:2] = [5, 6, 7]
print(a)

# Add list item
print("--Add--list--item--")
a = [1, 2, 3]
b = [5, 6, 7]
print(a)
a.append(4)
print(a)
a.insert(0, 0)
print(a)
a.extend(b)
print(a)
a.extend((100, 101, 102))
print(a)

# Remove list item
print("--Remove--list--item--")
a = [1, 2, 3]
print(a)
a.remove(1)
print(a)
a.pop()
print(a)
del a[0]
print(a)
a.clear()
print(a)

# Loop
print("--Loop--")
a = [1, 2, 3]
for item in a:
    print(item)
for i in range(len(a)):
    print(a[i])
[print(x) for x in a]

# Comprehension
print("--Comprehension--")
a = [1, 2, 3]
print(a)
newA = [(x + 1) for x in a]
print(newA)
newB = [(x+ 2) for x in a if x >= 2]
print(newB)
newC = []
newC.extend(a)
print(newC)

# Sort
print("--Sort--")
a = [1, 2, 3]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
def myFunc(n):
    if n % 2 == 0:
        return True
    else:
        return False
a.sort(key=myFunc)
print(a)

# Copy
print("--Copy--")
# Mutation
a = [1, 2, 3]
b = a
print(a==b)
b[0] = 4;
print(a, b)
# Immutation
a = [1, 2, 3]
b = list(a)
c = a.copy()
print(a==b)
print(a==c)
b[0] = 4;
c[0] = 4;
print(a, b, c)

# Join
print("--Join--")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
list1.extend(list2)
print(list1 + list2)