import re

def check_word_blank_capital(str):
    pattern = r'[a-zA-Z]+\ [A-Z]'
    return bool(re.fullmatch(pattern, str))

def check_email(email):
    pattern = r'([a-z0-9]+((_|.)?[a-z0-9]+)*)+\@[a-z0-9]+(\.[a-z]+)+'
    return bool(re.fullmatch(pattern, email))

def check_credit_card(credit_card):
    pattern = r'(([0-9]{4}\-){3}|([0-9]{4}\ ){3})[0-9]{4}'
    return bool(re.fullmatch(pattern, credit_card))

str = input('String: ')
print(check_word_blank_capital(str))

email = input('Email: ')
print(check_email(email))

credit_card = input('Credit card: ')
print(check_credit_card(credit_card))