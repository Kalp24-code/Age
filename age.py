from datetime import date


def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Get the user's birth year, month, and day
year = int(input("Enter your birth year : "))
month = int(input("Enter your birth month : "))
day = int(input("Enter your birth day : "))

# Create a date object for the birthdate
birthdate = date(year, month, day)

# Calculate the age
age = calculate_age(birthdate)
print(f"Your age is: {age}")
