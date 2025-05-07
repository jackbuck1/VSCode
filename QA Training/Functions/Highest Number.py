#Highest Number
def highest_number():
    first_number = int (input ("Please enter your first number: "))
    second_number = int (input ("Please enter your second number: "))
    third_number = int (input ("Please enter your third number: "))

    if first_number >= second_number and first_number >= third_number:
        return first_number
    elif second_number >= first_number and second_number >= third_number:
      return second_number
    else:
      return third_number

highest = highest_number()

print (f"The highest number that you input was {highest}")