# Single line string
x = "Hello world!"
print(x)

# Multi-line string
x = """
Hello world!
"""
print(x)

# Check the substring is contains
x = "Hello world!"
print("world" in x)

# Check the substring is not contains
x = "Hello world!"
print("hello" not in x)

# Get string length
x = "Hello world!"
print(len(x))

# Get char by index
x = "Hello world!"
print(x[0])

# Foreach for char's
x = "Hello world!"
for c in x:
    print(c)

# Conditional statement
x = "Hello world!"
if "Hello world!" in x:
    print("Yes")

# Slicing string
x = "Hello world!"
print(x[2:5])

# Slicing from the start
x = "Hello world!"
print(x[:5])

# Slicing to the end
x = "Hello world!"
print(x[5:])

# Negative index slicing
x = "Hello world!"
print(x[-5:-2])

# String to upper
x = "Hello world!"
print(x.upper())

# String to lower
x = "Hello world!"
print(x.lower())

# Remove whitespaces from the start and end
x = " Hello world! "
print(x.strip())

# Replace string
x = "Hello world!"
print(x.replace("world", "universe"))

# Split the string to list
x = "Hello world!"
print(x.split(" "))

# Concatenate string
x = "Hello"
y = " world!"
print(x + y)

# Format string
age = 36
txt = "I am {} years old."
print(txt.format(age))

# Format string with indexed place
age = 36
txt = "I am {1} years old."
print(txt.format(age, age + 1))

# Escape characters
x = "Hello world! \"Kek\""
print(x)