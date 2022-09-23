from math import sqrt

# def delete_multiples(number, lst):
#     i = 0
#     while i < len(lst):
#         if(number != lst[i] and lst[i] % number == 0):
#             lst.pop(i)
#         else:
#             i += 1

number = int(input("Introduzca un número: "))

# positive_numbers = []

# for i in range(2, number + 1):
#     positive_numbers.append(i)

# not_marked_index = 0
# while( prime_numbers[not_marked_index] * prime_numbers[not_marked_index] < number ):
#     delete_multiples(prime_numbers[not_marked_index], prime_numbers)
#     not_marked_index += 1
    
# print("Prime numbers between 2 and", number, "are", prime_numbers)

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