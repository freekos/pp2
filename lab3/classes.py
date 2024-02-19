# 1
class IO:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())

# io = IO()
# io.getString()
# io.printString()

# 2
# It's like abstract interface
class Shape:
    def area(self):
        pass
# TASK: The Square class has an init function
class Square(Shape):
    def __init__(self):
        self.length = 0
    def init(self, length):
        self.length = length
    def area(self):
        print(self.length ** 2)

# square = Square()
# square.init(10)
# square.area()

# 3
class Rectangle(Shape):
    # Class instance can be constructed by a length and width
    def __init__(self, width, length):
        self.width = width
        self.length = length
    # The Rectangle class has a method which can compute the area
    def area(self):
        return self.width * self.length
    
# rectangle = Rectangle(10, 10)
# print(rectangle.area())

# 4
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self) -> None:
        print(self.x, self.y)
    def move(self, dx, dy) -> None:
        self.x += dx
        self.y += dy
    def dist(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# point = Point(10, 10)
# point.show()
# point.move(1, 1)
# point.show()
# print(point.dist())

# 5
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

# account = Account("Alice")
# print(account.balance)
# account.deposit(100)
# print(account.balance)
# account.withdraw(150)
# print(account.balance)

# 6
is_prime = lambda x: all(x%i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1

# print(list(filter(is_prime, [2, 3, 5, 7, 8, 11, 13, 17, 19, 23])))
