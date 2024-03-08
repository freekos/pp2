# 1 Create a generator that generates the squares of numbers up to some number N.
def squares_seq_gen(n: int):
    for i in range(1, n+1):
        yield i ** 2

# for n in squares_gen(5):
#     print(n)

# 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_seq_gen(n: int):
    for i in range(1, n+1):
        yield i * 2
# for n in even_seq_gen(5):
#     print(n)

# 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def three_and_four_divisible_seq_gen(n: int):
    for i in range(0, n+1):
        if i%4 == 0 and i %3 == 0:
            yield i
# for n in three_and_four_divisible_seq_gen(12):
#     print(n)

# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares_range_gen(a: int, b: int):
    for i in range(a, b+1):
        yield i ** 2
# for n in squares_range_gen(1, 5):
#     print(n)

# 5 Implement a generator that returns all numbers from (n) down to 0.
def dec_seq_gen(n: int):
    for i in reversed(range(0, n+1)):
        yield i
# for n in dec_seq_gen(5):
#     print(n)