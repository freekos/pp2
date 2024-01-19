# Dynamic variables
x = 5
print(x)
x = 'string'
print(x)

# Casting data types
x = str(5)
y = int(5)
z = float(5)
print(x, y, z)

# Get data type
x = 5
m = "string"
print(type(x))
print(type(m))

# Case sensitive

a = 5
A = 10
print(a, A)

# Variables name
"""
Camelcase name
"""
myVariableName = "John"

"""
Pascal name
"""
MyVariableName = "John"

"""
Snake case
"""
my_variable_name = "John"

# Multiple variable names
a, b, c = 1, 2, 3;
print(a, b, c)

# Unpack a collection
a, b, c = [1, 2, 3]
print(a, b, c)

# Output examples
print(5 + 10)
print("Hello" + " World!")

# Incorrect output print(5 + "Hello")
# Correct output
print(str(5) + "Hello")

# Global variables
x = 5
def func1():
    print(x)
func1() 

def func2():
    global k;
    k = 10;
    print(k)
func2()
print(k)