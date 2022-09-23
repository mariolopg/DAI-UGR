import random
import re

def generate_string():
    square_bracket = ['[', ']']
    string = ''.join(random.choice(square_bracket) for i in range(random.randint(1, 10)))
    return string

def check_balance(str):
    balanced = 0
    is_balanced = True
    
    for i in range(0, len(str)):
        print(str[i])
        if str[i] == '[':
            balanced += 1
        else:
            if balanced == 0:
                is_balanced = False
                break
            else:
                balanced -= 1
    
    return is_balanced and balanced == 0           

string = generate_string()
print("Random string is", string)

is_balanced = check_balance(string)

if(is_balanced):
    print(string, "is balanced")
else:
    print(string, "is not balanced")