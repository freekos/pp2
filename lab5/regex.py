import re

# 1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def match_a_any_b(s: str):
    pattern = '^a(b*)$'
    if re.match(pattern, s):
        return True
    else:
        return False
# print(match_a_b("ab"))

# 2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def match_a_two_or_three_b(s: str):
    pattern = '^a(b{2,3})$'
    if re.match(pattern, s):
        return True
    else:
        return False
# print(match_a_bb("ab"))

# 3 Write a Python program to find sequences of lowercase letters joined with a underscore.
def find_lowercase_seq(s: str):
    pattern = '[a-z]+_[a-z]+'
    return re.findall(pattern, s)
# print(find_lowercase_seq("example_text"))

# 4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def find_uppercase_seq(s: str):
    pattern = '[A-Z][a-z]+'
    return re.findall(pattern, s)
# print(find_uppercase_seq("ExampleText"))

# 5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def match_a_anything_b(s: str):
    pattern = '^a.*b$'
    if re.match(pattern, s):
        return True
    else:
        return False
# print(match_a_anything_b("aab"))

# 6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace_with_colon(s: str):
    return re.sub(r'[ ,.]', ':', s)
# print(replace_with_colon("This is a test, . :"))

# 7 Write a python program to convert snake case string to camel case string.
def snake_to_camel(s: str):
    return ''.join(word.title() for word in s.split('_'))
# print(snake_to_camel("this_is_snake_case"))

# 8 Write a Python program to split a string at uppercase letters.
def split_at_uppercase(s: str):
    return re.findall('[A-Z][^A-Z]*', s)
# print(split_at_uppercase("SplitLetters"))

# 9 Write a Python program to insert spaces between words starting with capital letters.
def insert_spaces(s: str):
    return re.sub(r'([A-Z])', r' \1', s).strip()
# print(insert_spaces("InsertWords"))

# 10 Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(s: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
# print(camel_to_snake("CamelCase"))
