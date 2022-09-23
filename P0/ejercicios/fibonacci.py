with open("fibonacci_start.txt") as file:
    txt = file.read().splitlines()
    number = int(txt[0])
    
print("Your number is", number, ", calculating result...")
fibonacci = [0, 1]

for i in range(2, number):
    sumatory = fibonacci[i - 2] + fibonacci[i - 1]
    fibonacci.append(sumatory)
    
with open("fibonacci_result.txt", "w") as file:
    result = "The result is " + str(fibonacci[number - 1])
    file.write(result)
