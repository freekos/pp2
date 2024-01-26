# boolean operators
a = 4
b = 3
print(a==b)
print(a!= b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

# Conditions
a = 4
b = 3
if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")

# Convert to boolean
print(bool(4)) # True
print(bool("Hi")) # True
print(bool([1, 2, 3])) # True
print(bool("")) # False
print(bool(None)) # False
print(bool(0)) # False