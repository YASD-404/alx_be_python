FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celsius(fahrenheit):
    celsius= FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit-32)
    return celsius 
def convert_to_fahrenheit(celsius):
    fahrenheit=(CELSIUS_TO_FAHRENHEIT_FACTOR*celsius)+32
    return fahrenheit
temp=float(input("Enter the temperature to convert: "))
cel_fah=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
if cel_fah.lower() == "c":
    print(convert_to_celsius(temp))
elif cel_fah.lower()=="f":
    print(convert_to_fahrenheit(temp))
else:
    print("Invalid temperature. Please enter a numeric value.")

