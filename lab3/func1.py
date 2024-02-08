import random

# 1
def gram_to_ounce(grams: int) -> int:
    return grams * 28.3495231

# 2
def fahrenheit_centigrade(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

# 3
def get_chicken_and_rabbit_count(head_count: int, leg_count: int) -> (int, int):
    for chickens in range(head_count + 1):
        rabbits = head_count - chickens
        if 2 * chickens + 4 * rabbits == leg_count:
            return (chickens, rabbits)

# 4
def filter_primes(list: [int]) -> [int]:
    return [x for x in list if is_prime(x)]

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# 5
def get_permutations(input_str: str) -> [str]:
    result = []

    def backtrack(start):
        if start == len(input_str) - 1:
            result.append(''.join(input_str))
            return

        for i in range(start, len(input_str)):
            input_str[start], input_str[i] = input_str[i], input_str[start]
            backtrack(start + 1)
            input_str[start], input_str[i] = input_str[i], input_str[start]

    input_str = list(input_str)
    backtrack(0)

    return result

# 6
def reverse_words(input_str: str) -> str:
    if not isinstance(input_str, str):
        raise TypeError("input_str is not string")
    return " ".join(input_str.split(" ")[::-1])

# 7
def has_33(list: [int]) -> bool:
    return "33" in "".join(map(str, list))

# 8
def spy_game(list: [int]) -> bool:
    result = [x for x in list if(x == 0 or x == 7)]
    return "007" in "".join(map(str, result))

# 9
def circle_volume(radius: float) -> float:
    return 4 * 3.14 * radius ** 2

# 10
def unique_list(list: list) -> list:
    result = []
    for x in list:
        if x not in result:
            result.append(x)
    return result

# 11
def is_palindrome(input_str: str) -> bool:
    if not isinstance(input_str, str):
        raise TypeError("input_str is not string")
    return input_str == input_str[::-1]

# 12
def histogram(list: [int]) -> str:
    return "\n".join([x * '*' for x in list])

# 13
def start_guess_number_game():
    try:
        name = input("Hello! What is your name?\n")
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")
        target = random.randint(1, 20)

        while True:
            value = int(input("Take a guess.\n"))
            is_valid, message = guess_number_validate(target, value)
            if not is_valid:
                print(message)
            else:
                print("Good job, " + name + "! You guessed my number in " + str(target) + " guesses!")
                break
    except KeyboardInterrupt:
        print("Goodbye!")

def guess_number_validate(target: int, value: int) -> (bool, str):
    if(target == value):
        return (True, None)
    elif(target > value):
        return (False, "Your guess is too low.")
    else:
        return (False, "Your guess is too high.")

# 14
"""
For example you can check the test_func1.py file
"""