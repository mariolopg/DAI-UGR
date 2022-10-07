from math import sqrt

number = int(input("Introduzca un número: "))

positive_numbers = []
marked_numbers = []

for i in range(2, number + 1):
    positive_numbers.append(i)
    
for i in range(2, int(sqrt(number)) + 1):
    if i not in marked_numbers:
        for j in range(i, number // i + 1):
            marked_numbers.append(i * j)
            
prime_numbers = [i for i in positive_numbers if i not in marked_numbers]

print("Prime numbers between 2 and", number, "are", prime_numbers)