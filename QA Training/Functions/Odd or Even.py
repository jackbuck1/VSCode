#Odd or Even
def odd_or_even():
    number = int (input("Please enter a number: "))
    if number % 2 == 0:
        print(f"Your number {number} is Even")
    else: 
        print(f"Your number {number} is Odd")
    
odd_or_even()