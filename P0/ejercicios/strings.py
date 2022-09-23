import random
import re

def generate_string():
    square_bracket = ['[', ']']
    string = ''.join(random.choice(square_bracket) for i in range(random.randint(1, 10)))
    return string

def check_balance(str):
    pattern = r'(\[((\[\])*)\])*'
    return bool(re.fullmatch(pattern, str))

string = generate_string()
print("Random string is", string)

is_balanced = check_balance(string)

if(is_balanced):
    print(string, "is balanced")
else:
    print(string, "is not balanced")