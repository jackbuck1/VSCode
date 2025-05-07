#Temperature Converter
def tempconverter():
    temp = int(input("Please enter the temperature in degrees Celsius and I will convert it to Farenheit"))
    Farenheit = temp * (9/5) + 32
    print (f"The temperature in Farenheit is: {Farenheit}")

tempconverter()