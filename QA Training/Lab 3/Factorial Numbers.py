Number = int(input("Please enter a number and I will calculate it's factorial value: "))
Factorial = 1
i = 1

while i <= Number:
    Factorial *= i
    i += 1

print(f"The factorial of {Number} is {Factorial}")