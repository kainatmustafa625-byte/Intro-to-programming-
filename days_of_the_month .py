# Step 1: Dictionary for days in each month
month_days = {
    1: 31,  # January
    2: 28,  # February default (non-leap)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}
# Step 2: Ask for month number
month = int(input("Enter the month number (1-12): "))

if 1 <= month <= 12:
    # Step 3: Leap year adjustment for February
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
