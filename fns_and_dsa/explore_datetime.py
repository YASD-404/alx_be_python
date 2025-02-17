from datetime import datetime, timedelta
current_date=datetime.now()
def display_current_datetime():
    display=datetime.strftime(current_date,"%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {display}")
def calculate_future_date():
    number_of_days=int(input("Enter the number of days to add to the current date: "))
    future_date=current_date+timedelta(days=number_of_days)
    display=datetime.strftime(future_date,"%Y-%m-%d %H:%M:%S")
    print(f"Future date: {display}")
display_current_datetime()
calculate_future_date()


