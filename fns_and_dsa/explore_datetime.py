# from datetime import datetime, timedelta
# current_date=datetime.now()
# def display_current_datetime():
#     display=datetime.strftime(current_date,"%Y-%m-%d %H:%M:%S")
#     print(f"Current date and time: {display}")
# def calculate_future_date():
#     number_of_days=int(input("Enter the number of days to add to the current date: "))
#     future_date=current_date+timedelta(days=number_of_days)
#     display=datetime.strftime(future_date,"%Y-%m-%d %H:%M:%S")
#     print(f"Future date: {display}")
# display_current_datetime()
# calculate_future_date()


FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    try:
        
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F.")
        elif unit == "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
