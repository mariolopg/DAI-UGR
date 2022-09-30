#./app/app.py
from flask import Flask, render_template
import re
from math import sqrt

app = Flask(__name__)
          
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/square_brackets/<str>')
def strings(str):
    # Balanced se usa para controlar los corchetes que se abren y cierran, 0 = balanceado.
    balanced = 0
    stop_loop = True
    
    for i in range(0, len(str)):
        print(str[i])
        if str[i] == '[':
            balanced += 1
        else:
            # Si hay un corchete de cierre, ], y está balanceado a 0 quiere decir que no se a abierto uno previamente
            if balanced == 0:
                stop_loop = False
                break
            else:
                balanced -= 1
    
    is_balanced = stop_loop and balanced == 0
    
    result = str + " is balanced" 
    
    if not is_balanced:
        result = str + " is not balanced"
    
    return result

@app.route('/fibonacci/<int:number>')
def fibonacci(number):
    fibonacci = [0, 1]
    
    for i in range(2, number):
        sumatory = fibonacci[i - 2] + fibonacci[i - 1]
        fibonacci.append(sumatory)
        
    result = "Fibonacci result until " + str(number)  +  " is " + str(fibonacci[number - 1])
    return result

@app.route('/eratostenes/<int:number>')
def eratostenes(number):
    positive_numbers = []
    marked_numbers = []

    for i in range(2, number + 1):
        positive_numbers.append(i)
        
    for i in range(2, int(sqrt(number)) + 1):
        if i not in marked_numbers:
            for j in range(i, number // i + 1):
                marked_numbers.append(i * j)
                
    prime_numbers = [i for i in positive_numbers if i not in marked_numbers]

    result = "Prime numbers between 2 and " + str(number) + " are " + str(prime_numbers)
    return result
    
@app.route('/credit_card/<credit_card>')
def check_credit_card(credit_card):
    pattern = r'(([0-9]{4}\-){3}|([0-9]{4}\ ){3})[0-9]{4}'
    is_credit_card = bool(re.fullmatch(pattern, credit_card))
    
    result = credit_card + " is valid"
    
    if not is_credit_card:
        result = credit_card + " is not valid"
        
    return result

@app.route('/email/<email>')
def check_email(email):
    pattern = r'([a-z0-9]+((_|.)?[a-z0-9]+)*)+\@[a-z0-9]+(\.[a-z]+)+'
    is_valid = bool(re.fullmatch(pattern, email))
    
    result = email + " is valid"
    
    if not is_valid:
        result = email + " is not valid"
        
    return result

@app.route('/capital/<string>')
def check_word_blank_capital(string):
    pattern = r'[a-zA-Z]+\ [A-Z]'
    is_valid = bool(re.fullmatch(pattern, string))
    
    result = string + " is valid"
    
    if not is_valid:
        result = string + " is not valid"
        
    return result

@app.route('/image')
def image():
    return render_template('index.html')

# app name
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html')