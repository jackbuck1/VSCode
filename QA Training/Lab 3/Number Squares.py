number = 1

while number <= 100:
    square = number ** 2
    if square > 2000:
        break
    print(f"{number} and its square is {square}")
    number += 1